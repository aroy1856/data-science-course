# 1.   Creates a dictionary where student names are keys and their marks are values.
student_marks = {
    "Abhishek": 90,
    "Arijit": 85,
    "Anirban": 88,
    "Sagnik": 92,
    "Ayush": 95
}

# 2.   Asks the user to input a student's name.
student_name = input("Enter the student's name: ")

# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

if student_name in student_marks:
    print(f"{student_name}'s marks is {student_marks[student_name]}")
else:
    print("Student not found")
