import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import queue # For thread-safe communication with GUI

# Client Configuration
DEFAULT_SERVER_IP = '127.0.0.1' # Default server IP for convenience
DEFAULT_SERVER_PORT = 12345     # Default server Port for convenience
BUFFER_SIZE = 1024

message_queue = queue.Queue() # Queue for messages to be displayed on GUI

class ChatClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python Chat Client")
        master.geometry("550x650") # Increased size
        master.resizable(True, True)
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.client_socket = None
        self.receive_thread = None
        self.is_connected = False
        self.client_name = ""
        
        # Styling
        self.master.option_add('*Font', 'Arial 10')
        self.master.option_add('*Button.Font', 'Arial 10 bold')
        self.master.option_add('*Label.Font', 'Arial 10')
        self.master.option_add('*Entry.Font', 'Arial 10')
        self.master.option_add('*ScrolledText.Font', 'Consolas 9') # Monospace for chat
        
        # Connection/Name Frame
        self.conn_name_frame = tk.Frame(master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
        self.conn_name_frame.pack(fill=tk.X, pady=5)
        
        self.name_label = tk.Label(self.conn_name_frame, text="Your Name:")
        self.name_label.pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(self.conn_name_frame, width=15, relief=tk.FLAT, bd=1, bg="white", fg="#333")
        self.name_entry.pack(side=tk.LEFT, padx=5)
        self.name_entry.insert(0, "Guest") # Default name
        
        self.ip_label = tk.Label(self.conn_name_frame, text="Server IP:")
        self.ip_label.pack(side=tk.LEFT, padx=5)
        self.ip_entry = tk.Entry(self.conn_name_frame, width=12, relief=tk.FLAT, bd=1, bg="white", fg="#333")
        self.ip_entry.pack(side=tk.LEFT, padx=5)
        self.ip_entry.insert(0, DEFAULT_SERVER_IP)
        
        self.port_label = tk.Label(self.conn_name_frame, text="Port:")
        self.port_label.pack(side=tk.LEFT, padx=5)
        self.port_entry = tk.Entry(self.conn_name_frame, width=7, relief=tk.FLAT, bd=1, bg="white", fg="#333")
        self.port_entry.pack(side=tk.LEFT, padx=5)
        self.port_entry.insert(0, str(DEFAULT_SERVER_PORT))
        
        # Connect/Disconnect Buttons
        self.button_frame = tk.Frame(master, padx=5, pady=5)
        self.button_frame.pack(fill=tk.X)
        self.connect_button = tk.Button(self.button_frame, text="Connect", command=self.connect_to_server, bg="#4CAF50", fg="white")
        self.connect_button.pack(side=tk.LEFT, padx=10, pady=5, expand=True)
        self.disconnect_button = tk.Button(self.button_frame, text="Disconnect", command=self.disconnect_from_server, state=tk.DISABLED, bg="#f44336", fg="white")
        self.disconnect_button.pack(side=tk.LEFT, padx=10, pady=5, expand=True)
        
        self.status_label = tk.Label(master, text="Status: Disconnected", fg="red", font='Arial 10 bold')
        self.status_label.pack(pady=5)
        
        # Chat Display Area
        self.chat_label = tk.Label(master, text="Chat History:", font='Arial 10 bold')
        self.chat_label.pack(pady=(10, 0))
        self.chat_display = scrolledtext.ScrolledText(master, state='disabled', wrap=tk.WORD, bg="#e8f4f8", fg="#333", relief=tk.SUNKEN, bd=2)
        self.chat_display.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        
        # Message Input Area
        self.message_input_frame = tk.Frame(master, bd=2, relief=tk.GROOVE, padx=5, pady=5)
        self.message_input_frame.pack(fill=tk.X, pady=5)
        self.message_entry = tk.Entry(self.message_input_frame, width=40, relief=tk.FLAT, bd=1, bg="white", fg="#333")
        self.message_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.message_entry.bind("<Return>", self.send_message_event) # Bind Enter key to send
        
        self.send_button = tk.Button(self.message_input_frame, text="Send", command=self.send_message, bg="#2196F3", fg="white")
        self.send_button.pack(side=tk.RIGHT, padx=5)
        
        self.set_ui_state(connected=False) # Initial UI state
        
        # Start checking message queue periodically
        self.master.after(100, self.process_queue)

    def set_ui_state(self, connected):
        """Adjusts UI elements based on connection status."""
        self.is_connected = connected
        if connected:
            self.name_entry.config(state=tk.DISABLED)
            self.ip_entry.config(state=tk.DISABLED)
            self.port_entry.config(state=tk.DISABLED)
            self.connect_button.config(state=tk.DISABLED)
            self.disconnect_button.config(state=tk.NORMAL)
            self.message_entry.config(state=tk.NORMAL)
            self.send_button.config(state=tk.NORMAL)
            self.status_label.config(text="Status: Connected", fg="green")
            self.message_entry.focus_set() # Focus on message input for immediate typing
        else:
            self.name_entry.config(state=tk.NORMAL)
            self.ip_entry.config(state=tk.NORMAL)
            self.port_entry.config(state=tk.NORMAL)
            self.connect_button.config(state=tk.NORMAL)
            self.disconnect_button.config(state=tk.DISABLED)
            self.message_entry.config(state=tk.DISABLED)
            self.send_button.config(state=tk.DISABLED)
            self.status_label.config(text="Status: Disconnected", fg="red")

    def display_message(self, message):
        """Appends a message to the chat display with a timestamp."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, formatted_message + "\n")
        self.chat_display.yview(tk.END)
        self.chat_display.config(state='disabled')

    def connect_to_server(self):
        """Initiates connection to the server."""
        self.client_name = self.name_entry.get().strip()
        if not self.client_name:
            messagebox.showerror("Error", "Please enter your name to join the chat.")
            return
        
        server_ip = self.ip_entry.get().strip()
        server_port_str = self.port_entry.get().strip()
        if not server_ip or not server_port_str:
            messagebox.showerror("Error", "Server IP and Port are required.")
            return
        
        try:
            server_port = int(server_port_str)
            if not (1024 <= server_port <= 65535):
                raise ValueError("Port number out of valid range (1024-65535).")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid Port number: {e}")
            return
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.client_socket.connect((server_ip, server_port))
            self.set_ui_state(connected=True)
            self.display_message(f"--- Connected to {server_ip}:{server_port} as '{self.client_name}' ---")
            # Send client name to server immediately after connection
            self.client_socket.sendall(f"NAME: {self.client_name}".encode('utf-8'))
            
            self.receive_thread = threading.Thread(target=self.receive_messages)
            self.receive_thread.daemon = True # Allow main program to exit
            self.receive_thread.start()
        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Connection refused. Make sure the server is running and reachable.")
            self.set_ui_state(connected=False)
        except Exception as e:
            messagebox.showerror("Connection Error", f"An unexpected error occurred during connection: {e}")
            self.set_ui_state(connected=False)

    def disconnect_from_server(self):
        """Disconnects from the server."""
        if self.client_socket:
            try:
                # Send a disconnect message to the server
                self.client_socket.sendall(f"<{self.client_name}> has left the chat.".encode('utf-8'))
                self.client_socket.shutdown(socket.SHUT_RDWR)
                self.client_socket.close()
            except OSError:
                pass
            except Exception as e:
                print(f"Error during socket shutdown/close: {e}")
            self.client_socket = None
            self.set_ui_state(connected=False)
            self.display_message("--- Disconnected from server ---")
            self.client_name = ""

    def receive_messages(self):
        """Thread function to continuously receive messages from the server."""
        while self.is_connected:
            try:
                message = self.client_socket.recv(BUFFER_SIZE).decode('utf-8')
                if not message:
                    message_queue.put("[DISCONNECTED] Server disconnected. Please reconnect.")
                    self.master.after(0, self.disconnect_from_server)
                    break
                message_queue.put(message)
            except ConnectionResetError:
                message_queue.put("[DISCONNECTED] Server reset connection. Please reconnect.")
                self.master.after(0, self.disconnect_from_server)
                break
            except Exception as e:
                message_queue.put(f"[ERROR] Error receiving message: {e}")
                self.master.after(0, self.disconnect_from_server)
                break

    def send_message_event(self, event=None):
        """Handles sending message when Enter key is pressed."""
        self.send_message()

    def send_message(self):
        """Sends the message from the input field to the server."""
        if not self.is_connected or not self.client_socket:
            messagebox.showwarning("Not Connected", "You are not connected to the server.")
            return
        
        message = self.message_entry.get().strip()
        if not message:
            return
        
        try:
            self.client_socket.sendall(message.encode('utf-8'))
            self.display_message(f"You: {message}")
            self.message_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Send Error", f"Failed to send message: {e}")
            self.disconnect_from_server()

    def process_queue(self):
        """Periodically checks the message queue and updates the GUI."""
        while not message_queue.empty():
            message = message_queue.get()
            self.display_message(message)
        self.master.after(100, self.process_queue)

    def on_closing(self):
        """Handles closing the Tkinter window."""
        if self.is_connected:
            if messagebox.askokcancel("Quit Chat", "You are connected. Do you want to disconnect and quit?"):
                self.disconnect_from_server()
                self.master.destroy()
        else:
            if messagebox.askokcancel("Quit Chat", "Do you want to quit?"):
                self.master.destroy()

if __name__ == "__main__":
    from datetime import datetime
    root = tk.Tk()
    app = ChatClientGUI(root)
    root.mainloop()