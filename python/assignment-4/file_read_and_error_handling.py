
try:
    with open("sample.txt", "r") as file:
        for i, line in enumerate(file):
            print(f"Line {i+1}: {line}")
except FileNotFoundError:
    print("The file 'sample.txt' not found")
except Exception as e:
    print(f"An error occurred: {e}")
    
