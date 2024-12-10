import csv

# Parent class Employee
class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

# Child class Manager
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

# Child class Worker
class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

# File handling functions
def save_employees_to_csv(filename, employees):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Salary", "Department", "Hours Worked"])
        for emp in employees:
            if isinstance(emp, Manager):
                writer.writerow([emp.get_name(), emp.get_age(), emp.get_salary(), emp.get_department(), ""])
            elif isinstance(emp, Worker):
                writer.writerow([emp.get_name(), emp.get_age(), emp.get_salary(), "", emp.get_hours_worked()])

def load_employees_from_csv(filename):
    employees = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Department"]:
                    employees.append(Manager(row["Name"], int(row["Age"]), float(row["Salary"]), row["Department"]))
                elif row["Hours Worked"]:
                    employees.append(Worker(row["Name"], int(row["Age"]), float(row["Salary"]), int(row["Hours Worked"])))
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    return employees

def add_employee(employees):
    emp_type = input("Enter employee type (Manager/Worker): ").strip().lower()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    if emp_type == "manager":
        department = input("Enter department: ")
        employees.append(Manager(name, age, salary, department))
    elif emp_type == "worker":
        hours_worked = int(input("Enter hours worked: "))
        employees.append(Worker(name, age, salary, hours_worked))
    else:
        print("Invalid employee type.")

def display_employees(employees):
    for emp in employees:
        print(f"Name: {emp.get_name()}, Age: {emp.get_age()}, Salary: {emp.get_salary()}", end='')
        if isinstance(emp, Manager):
            print(f", Department: {emp.get_department()}")
        elif isinstance(emp, Worker):
            print(f", Hours Worked: {emp.get_hours_worked()}")

def update_employee(employees):
    name = input("Enter the name of the employee to update: ")
    for emp in employees:
        if emp.get_name() == name:
            emp.set_age(int(input("Enter new age: ")))
            emp.set_salary(float(input("Enter new salary: ")))
            if isinstance(emp, Manager):
                emp.set_department(input("Enter new department: "))
            elif isinstance(emp, Worker):
                emp.set_hours_worked(int(input("Enter new hours worked: ")))
            print("Employee updated successfully.")
            return
    print("Employee not found.")

def delete_employee(employees):
    name = input("Enter the name of the employee to delete: ")
    for emp in employees:
        if emp.get_name() == name:
            employees.remove(emp)
            print("Employee deleted successfully.")
            return
    print("Employee not found.")

# User interface
def menu():
    filename = "employees.csv"
    employees = load_employees_from_csv(filename)

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            display_employees(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            save_employees_to_csv(filename, employees)
            print("Changes saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()