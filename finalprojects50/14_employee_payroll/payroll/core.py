import csv
from payroll.decorators import admin_only

class Employee:
    def __init__(self, emp_id, name, hours, rate):
        if hours < 0 or rate < 0:
            raise ValueError("Hours and rate must be non-negative.")
        self.emp_id = emp_id
        self.name = name
        self.hours = hours
        self.rate = rate

    def compute_salary(self):
        overtime_hours = max(0, self.hours - 40)
        regular_hours = self.hours - overtime_hours
        overtime_pay = overtime_hours * self.rate * 1.5
        gross_salary = regular_hours * self.rate + overtime_pay
        tax = self._apply_tax(gross_salary)
        net_salary = gross_salary - tax
        return {
            "gross_salary": gross_salary,
            "tax": tax,
            "net_salary": net_salary,
            "overtime_hours": overtime_hours
        }

    def _apply_tax(self, salary):
        # Simple progressive tax brackets
        if salary <= 30000:
            tax = salary * 0.1
        elif salary <= 70000:
            tax = 3000 + (salary - 30000) * 0.2
        else:
            tax = 11000 + (salary - 70000) * 0.3
        return tax

    def __str__(self):
        return f"Employee({self.emp_id}): {self.name}"

class Payroll:
    def __init__(self):
        self.employees = {}
        self.is_admin = False  # Flag for admin access

    def add_employee(self, emp_id, name, hours, rate):
        try:
            emp = Employee(emp_id, name, hours, rate)
            self.employees[emp_id] = emp
            print(f"✅ Added {emp}")
        except ValueError as e:
            print(f"⚠️ Error adding employee: {e}")

    @admin_only
    def update_salary(self, emp_id, hours=None, rate=None):
        emp = self.employees.get(emp_id)
        if not emp:
            print(f"⚠️ Employee {emp_id} not found.")
            return
        if hours is not None:
            if hours < 0:
                print("⚠️ Hours cannot be negative.")
                return
            emp.hours = hours
        if rate is not None:
            if rate < 0:
                print("⚠️ Rate cannot be negative.")
                return
            emp.rate = rate
        print(f"✅ Updated {emp}")

    def generate_payslips(self):
        for emp in self.employees.values():
            salary_data = emp.compute_salary()
            print(f"\nPayslip for {emp.name} (ID: {emp.emp_id}):")
            print(f"  Gross Salary: ₹{salary_data['gross_salary']:.2f}")
            print(f"  Tax Deducted: ₹{salary_data['tax']:.2f}")
            print(f"  Net Salary: ₹{salary_data['net_salary']:.2f}")
            print(f"  Overtime Hours: {salary_data['overtime_hours']}")

    def overtime_employees(self):
        # Generator yielding employees with overtime
        for emp in self.employees.values():
            if emp.hours > 40:
                yield emp

    def export_to_csv(self, filename="payroll.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Name", "Hours", "Rate", "Gross Salary", "Tax", "Net Salary", "Overtime Hours"])
            for emp in self.employees.values():
                salary_data = emp.compute_salary()
                writer.writerow([
                    emp.emp_id,
                    emp.name,
                    emp.hours,
                    emp.rate,
                    f"{salary_data['gross_salary']:.2f}",
                    f"{salary_data['tax']:.2f}",
                    f"{salary_data['net_salary']:.2f}",
                    salary_data['overtime_hours']
                ])
        print(f"✅ Payroll exported to {filename}")

    def login_admin(self, password):
        # For demo: password is 'admin123'
        if password == 'admin123':
            self.is_admin = True
            print("🔐 Admin access granted.")
        else:
            print("❌ Incorrect password.")
