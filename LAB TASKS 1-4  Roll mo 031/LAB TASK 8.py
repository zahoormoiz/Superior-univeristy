LAB TASK 8
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Parent class Employee
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

# Child class Staff inheriting from both Person and Employee
class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")

# File handling functions
def save_employee_to_file(filename, staff):
    with open(filename, 'a') as file:
        file.write(f"{staff.name},{staff.age},{staff.employee_id},{staff.position},{staff.department}\n")

def read_employees_from_file(filename):
    employees = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, age, employee_id, position, department = line.strip().split(',')
                employees.append(Staff(name, int(age), employee_id, position, department))
    except FileNotFoundError:
        print("File not found. No data to read.")
    return employees

def add_new_employee(filename):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    employee_id = input("Enter employee ID: ")
    position = input("Enter position: ")
    department = input("Enter department: ")

    new_staff = Staff(name, age, employee_id, position, department)
    save_employee_to_file(filename, new_staff)
    print("Employee information saved successfully.")

# Example usage
if __name__ == "__main__":
    filename = "employees.txt"

    # Add a new employee
    add_new_employee(filename)

    # Read employees from file
    employees = read_employees_from_file(filename)

    # Display all employee information
    for emp in employees:
        emp.display_info()
        emp.additional_info()
        print()
