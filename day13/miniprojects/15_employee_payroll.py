# 15. Employee Payroll System

# Concepts: Inheritance, Static Method, Polymorphism
# Classes:  Employee,  FullTimeEmployee,  PartTimeEmployee,  Payroll
# Requirements:
# Calculate salary based on hours/days
# Use @staticmethod for tax
# Use overriding for calculate_salary()

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must override calculate_salary method")

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

    @staticmethod
    def calculate_tax(amount):
        tax_rate = 10  # 10% tax
        return amount * tax_rate / 100

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary  # INR

    def calculate_salary(self):
        tax = Employee.calculate_tax(self.monthly_salary)
        net_salary = self.monthly_salary - tax
        print(f"{self.name}'s gross salary: ₹{self.monthly_salary}, Tax: ₹{tax}, Net: ₹{net_salary}")
        return net_salary

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate  # INR per hour

    def calculate_salary(self):
        gross_salary = self.hours_worked * self.hourly_rate
        tax = Employee.calculate_tax(gross_salary)
        net_salary = gross_salary - tax
        print(f"{self.name}'s gross salary: ₹{gross_salary}, Tax: ₹{tax}, Net: ₹{net_salary}")
        return net_salary

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_payroll(self):
        print("Processing payroll...")
        for emp in self.employees:
            emp.calculate_salary()

def main():
    payroll = Payroll()

    ft_emp = FullTimeEmployee(1, "Nisha", 50000)
    pt_emp = PartTimeEmployee(2, "Ravi", 80, 300)

    payroll.add_employee(ft_emp)
    payroll.add_employee(pt_emp)

    payroll.process_payroll()

if __name__ == "__main__":
    main()
