# 1.   Takes user input and writes it to a file named output.txt.
txt = input("Enter text to write into file: ")
with open("output.txt", "w") as file:
    file.writelines(txt)
    print("File has been written successfully")

# 2.   Appends additional data to the same file.
txt2 = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.writelines(txt2)
    print("Additional data has been appended successfully")
    
# 3.   Reads and displays the final content of the file.
with open("output.txt", "r") as file:
    print(file.read())
    print("File has been read successfully")
