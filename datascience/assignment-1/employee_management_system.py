employee_data = {
    101: {
        'name': 'Satya',
        'age': 27,
        'department': 'HR',
        'salary': 50000
    },
    102: {
        'name': 'Raj',
        'age': 30,
        'department': 'IT',
        'salary': 60000
    },
    103: {
        'name': 'Kumar',
        'age': 25,
        'department': 'HR',
        'salary': 55000
    },
    104: {
        'name': 'Rajesh',
        'age': 28,
        'department': 'IT',
        'salary': 65000
    },
    105: {
        'name': 'Suresh',
        'age': 29,
        'department': 'HR',
        'salary': 52000
    }
}


def add_employee():
    while True:
        employee_id = int(input("Enter employee ID: "))
        if employee_id in employee_data:
            print(f"Employee ID {employee_id} already exists. Please enter a new ID.")
            continue
        break

    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = int(input("Enter employee salary: "))

    employee_data[employee_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"Employee {name} added successfully.")


def search_employee():
    employee_id = int(input("Enter employee ID: "))
    if employee_id not in employee_data:
        print("Employee not found.")
        return

    employee = employee_data[employee_id]
    print("\nEmployee Details")
    print("-" * 40)
    print(f"{'ID':<12}: {employee_id}")
    print(f"{'Name':<12}: {employee['name']}")
    print(f"{'Age':<12}: {employee['age']}")
    print(f"{'Department':<12}: {employee['department']}")
    print(f"{'Salary':<12}: {employee['salary']}")
    print("-" * 40)


def view_employees():
    if not employee_data:
        print("No employees available.")
        return

    headers = ("ID", "Name", "Age", "Department", "Salary")
    rows = [
        (
            str(emp_id),
            emp['name'],
            str(emp['age']),
            emp['department'],
            str(emp['salary']),
        )
        for emp_id, emp in employee_data.items()
    ]

    col_widths = [
        max(len(headers[i]), max(len(row[i]) for row in rows))
        for i in range(len(headers))
    ]

    def format_row(row):
        return " | ".join(value.ljust(col_widths[i]) for i, value in enumerate(row))

    separator = "-+-".join("-" * width for width in col_widths)

    print()
    print(format_row(headers))
    print(separator)
    for row in rows:
        print(format_row(row))
    print()


def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for an Employee")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
