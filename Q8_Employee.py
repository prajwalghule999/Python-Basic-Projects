# Q8: Employee Management System

class Employee:

    # Constructor
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)   # Tuple

    # Method to display employee details
    def show_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])


# Dictionary to store employee objects
employees = {}

# Add 3 employees
for i in range(3):
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, department, salary)
    employees[emp_id] = emp

# Display all employees
print("\n----- Employee Details -----")

for emp in employees.values():
    emp.show_details()