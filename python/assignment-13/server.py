import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import queue 

# --- Server Configuration ---
SERVER_IP = '0.0.0.0' # Listen on all available network interfaces
SERVER_PORT = 12345
BUFFER_SIZE = 1024
MAX_CLIENTS = 10 # Maximum number of clients the server can handle

# List to keep track of connected clients (client_socket, address, name)
# Use a lock to ensure thread-safe access to this list
clients = []
clients_lock = threading.Lock()
# Queue for messages to be displayed on the GUI (from background threads)
message_queue = queue.Queue()

class ChatServerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python Chat Server")
        master.geometry("700x600")
        master.resizable(True, True)
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.is_server_running = False
        self.server_socket = None
        self.server_thread = None
        # --- Styling ---
        self.master.option_add('*Font', 'Arial 10')
        self.master.option_add('*Button.Font', 'Arial 10 bold')
        self.master.option_add('*Label.Font', 'Arial 10')
        self.master.option_add('*Entry.Font', 'Arial 10')
        self.master.option_add('*ScrolledText.Font', 'Consolas 9')
        # --- Top Frame for Controls ---
        self.control_frame = tk.Frame(self.master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
        self.control_frame.pack(fill=tk.X, pady=5)
        self.status_label = tk.Label(self.control_frame, text="Server Status: Not Running", fg="red", font='Arial 12 bold')
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)
        self.start_button = tk.Button(self.control_frame, text="Start Server", command=self.start_server_gui, bg="#4CAF50", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(self.control_frame, text="Stop Server", command=self.stop_server_gui, state=tk.DISABLED, bg="#f44336", fg="white")
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.clear_button = tk.Button(self.control_frame, text="Clear Log", command=self.clear_log, bg="#2196F3", fg="white")
        self.clear_button.pack(side=tk.RIGHT, padx=5)
        # --- Server Broadcast Input ---
        self.broadcast_frame = tk.Frame(self.master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
        self.broadcast_frame.pack(fill=tk.X, pady=5)
        self.message_entry = tk.Entry(self.broadcast_frame, width=50, relief=tk.FLAT, bd=1, bg="white", fg="#333")
        self.message_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.message_entry.bind("<Return>", self.send_broadcast_message_event) # Bind Enter key
        self.send_button = tk.Button(self.broadcast_frame, text="Broadcast", command=self.send_broadcast_message, bg="#FFC107", fg="black")
        self.send_button.pack(side=tk.RIGHT, padx=5)
        # --- Chat Log Display ---
        self.log_frame = tk.Frame(self.master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
        self.log_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        self.log_label = tk.Label(self.log_frame, text="Server Log & Broadcast History:", font='Arial 10 bold')
        self.log_label.pack(pady=(10, 0))
        self.log_text = scrolledtext.ScrolledText(self.master, state='disabled', wrap=tk.WORD, bg="#f0f0f0", fg="#333", relief=tk.SUNKEN, bd=2)
        self.log_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

    def clear_log(self):
        """Clears the content of the log text widget."""
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state='disabled')
        
    def start_server_gui(self):
        """Starts the server in a separate thread."""
        if not self.is_server_running:
            self.is_server_running = True
            self.status_label.config(text="Server Status: Starting...", fg="orange")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.message_entry.config(state=tk.NORMAL)
            self.send_button.config(state=tk.NORMAL)
            self.server_thread = threading.Thread(target=self._run_server)
            self.server_thread.daemon = True # Allows main program to exit even if thread is running
            self.server_thread.start()
            self.log_message(f"Attempting to start server on {SERVER_IP}:{SERVER_PORT}")

    def stop_server_gui(self):
        """Stops the server and cleans up."""
        if self.is_server_running:
            self.is_server_running = False
            self.status_label.config(text="Server Status: Stopping...", fg="orange")
            self.stop_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
            self.message_entry.config(state=tk.DISABLED)
            self.send_button.config(state=tk.DISABLED)
            # Close server socket to break accept() loop
            if self.server_socket:
                try:
                    self.server_socket.shutdown(socket.SHUT_RDWR)
                    self.server_socket.close()
                except OSError as e:
                    self.log_message(f"Error shutting down server socket: {e}")
                    self.server_socket = None
            # Close all client sockets
            with clients_lock:
                for client_sock, _, _ in clients: # Iterate (socket, address, name)
                    try:
                        client_sock.shutdown(socket.SHUT_RDWR)
                        client_sock.close()
                    except OSError:
                        pass # Ignore errors if already closed
                clients.clear()
                self.log_message("Server stopped.")
                self.status_label.config(text="Server Status: Not Running", fg="red")
                
    def _run_server(self):
        """Actual server logic running in a separate thread."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((SERVER_IP, SERVER_PORT))
            self.server_socket.listen(MAX_CLIENTS)
            message_queue.put(f"[SERVER] Server listening on {SERVER_IP}:{SERVER_PORT}")
            self.master.after(0, lambda: self.status_label.config(text="Server Status: Running", fg="green"))
            while self.is_server_running:
                try:
                    self.server_socket.settimeout(0.5) # Set a small timeout to check self.is_server_running
                    client_socket, client_address = self.server_socket.accept()
                    # Check if max clients reached
                    with clients_lock:
                        if len(clients) >= MAX_CLIENTS:
                            message_queue.put(f"[SERVER] Max clients reached. Refusing connection from {client_address}.")
                            client_socket.sendall("Server is full. Please try again later.".encode('utf-8'))
                            client_socket.close()
                            continue
                    # Start a new thread for each client
                    client_handler = threading.Thread(target=self._handle_client, args=(client_socket, client_address))
                    client_handler.daemon = True
                    client_handler.start()
                    message_queue.put(f"[SERVER] Accepted connection from {client_address}. Active threads: {threading.active_count() - 2}") # -2 for main and server thread
                except socket.timeout:
                    continue # Timeout occurred, check self.is_server_running again
                except OSError as e:
                    if self.is_server_running: # Only log if not intentionally stopped
                        message_queue.put(f"[ERROR] Server accept error: {e}")
                    break # Break loop on other OS errors (e.g., socket closed)
                except Exception as e:
                    message_queue.put(f"[ERROR] Unexpected error in server loop: {e}")
                    break   
        except socket.error as e:
            message_queue.put(f"[ERROR] Server socket binding/setup error: {e}")
            self.master.after(0, lambda: self.status_label.config(text="Server Status: Error", fg="red"))
        finally:
            if self.server_socket:
                self.server_socket.close()
                message_queue.put("[SERVER] Server socket closed.")
                self.master.after(0, lambda:
                self.status_label.config(text="Server Status: Not Running", fg="red"))
                self.master.after(0, lambda:
                self.start_button.config(state=tk.NORMAL))
                self.master.after(0, lambda:
                self.stop_button.config(state=tk.DISABLED))

    def _handle_client(self, client_socket, client_address):
        """Handles communication with a single client in its own thread."""
        client_name = f"Client-{client_address[1]}" # Default name
        try:
            # First message from client should be their name
            initial_data = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if initial_data.startswith("NAME:"):
                client_name = initial_data[len("NAME:"):]
                message_queue.put(f"[SERVER] Client {client_address} identified as '{client_name}'.")
                self._broadcast_message(f"'{client_name}' has joined the chat.", "SERVER")
            else:
                message_queue.put(f"[SERVER] Client {client_address} sent unexpected initial data. Assuming name '{client_name}'.")
                # Handle the first message as a regular message if not a name
                message_queue.put(f"[{client_name}] {initial_data}")
                self._broadcast_message(initial_data, client_name)
                with clients_lock:
                    clients.append((client_socket, client_address, client_name))
                while self.is_server_running:
                    message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
                    if not message: # Client disconnected
                        break
                    message_queue.put(f"[{client_name}] {message}")
                    self._broadcast_message(message, client_name)
        except ConnectionResetError:
            message_queue.put(f"[DISCONNECTED] Client '{client_name}'({client_address}) reset connection.")
        except Exception as e:
            message_queue.put(f"[ERROR] Error handling client'{client_name}' ({client_address}): {e}")
        finally:
            with clients_lock:
                if (client_socket, client_address, client_name) in clients:
                    clients.remove((client_socket, client_address, client_name))
                    try:
                        client_socket.close()
                    except OSError:
                        pass # Ignore if already closed
                    message_queue.put(f"[DISCONNECTED] Client '{client_name}' ({client_address}) left.")
                    self._broadcast_message(f"'{client_name}' has left the chat.", "SERVER")

    def _broadcast_message(self, message, sender_name):
        """Sends a message to all connected clients except the sender."""
        # Format message as it should appear on clients
        full_message = f"<{sender_name}> {message}".encode('utf-8')
        with clients_lock:
            clients_to_remove = []
            for client_sock, addr, name in clients:
                if name != sender_name: # Don't send back to sender
                    try:
                        client_sock.sendall(full_message)
                    except Exception as e:
                        message_queue.put(f"[BROADCAST ERROR] Could not send to '{name}' ({addr}): {e}")
                        clients_to_remove.append((client_sock, addr, name))
                # Mark for removal
                # Remove clients that failed to receive
            for client_sock, addr, name in clients_to_remove:
                if (client_sock, addr, name) in clients: # Check again in case it was already removed by its handler
                    clients.remove((client_sock, addr, name))
                    try:
                        client_sock.close()
                    except OSError:
                        pass # Ignore if already closed
                    message_queue.put(f"[CLEANUP] Removed disconnected client '{name}' ({addr}).")

    def send_broadcast_message_event(self, event=None):
        """Handles sending broadcast message when Enter key is pressed."""
        self.send_broadcast_message()

    def send_broadcast_message(self):
        """Sends the message from the server's input field to all connected clients."""
        if not self.is_server_running:
            messagebox.showwarning("Server Not Running", "Server must be running to broadcast messages.")
            return
        message = self.message_entry.get().strip()
        if not message:
            return # Don't send empty messages
        self.log_message(message, sender="SERVER (Broadcast)") # Log server's own message
        self._broadcast_message(message, "SERVER") # Send to all clients
        self.message_entry.delete(0, tk.END) # Clear input field

    def process_queue(self):
        """Periodically checks the message queue and updates the GUI."""
        while not message_queue.empty():
            message = message_queue.get()
            self.log_message(message, sender="SERVER Log") # Use a distinct sender for internal logs
            self.master.after(100, self.process_queue) # Check again after 100ms

    def on_closing(self):
        """Handles closing the Tkinter window."""
        if self.is_server_running:
            if messagebox.askokcancel("Quit Server", "Server is running. Do you want to stop it and quit?"):
                self.stop_server_gui() # Ensure server is stopped gracefully
                self.master.destroy()
            else:
                self.master.destroy()
    def log_message(self, message, sender="SERVER"):
        """Logs a message to the GUI log text widget."""
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sender}] {message}\n")
        self.log_text.config(state='disabled')
        self.log_text.see(tk.END)

if __name__ == "__main__":
    from datetime import datetime # Import here for logging timestamps
    root = tk.Tk()
    app = ChatServerGUI(root)
    root.mainloop()