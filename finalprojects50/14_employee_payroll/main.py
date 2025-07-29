# 14. Employee Payroll System 
# Objective: Calculate salaries with deductions. 
# Requirements: 
#  OOP: Employee class (name, hours, rate). 
#  Dictionary: Store employees (ID: Employee object). 
#  File Handling: Export payroll to CSV. 
#  Exception Handling: Negative hours/rate. 
#  Functions: Compute salary (overtime bonus if >40 hours). 
#  Conditionals: Apply tax brackets. 
#  Loops: Generate payslips for all employees. 
#  Generator: Yield employees with overtime. 
#  Decorator: @admin_only for salary updates. 


from payroll.core import Payroll

def main():
    payroll = Payroll()

    print("👔 Employee Payroll System")

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Update Employee Salary (Admin only)")
        print("3. Generate Payslips")
        print("4. List Employees with Overtime")
        print("5. Export Payroll to CSV")
        print("6. Admin Login")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            emp_id = input("Enter Employee ID: ").strip()
            name = input("Enter Name: ").strip()
            try:
                hours = float(input("Enter Hours Worked: ").strip())
                rate = float(input("Enter Hourly Rate: ").strip())
            except ValueError:
                print("⚠️ Invalid input for hours or rate.")
                continue
            payroll.add_employee(emp_id, name, hours, rate)

        elif choice == '2':
            if not payroll.is_admin:
                print("⚠️ Please login as admin first.")
                continue
            emp_id = input("Enter Employee ID to update: ").strip()
            try:
                hours = input("Enter new hours worked (leave blank to skip): ").strip()
                rate = input("Enter new hourly rate (leave blank to skip): ").strip()
                hours_val = float(hours) if hours else None
                rate_val = float(rate) if rate else None
            except ValueError:
                print("⚠️ Invalid input for hours or rate.")
                continue
            payroll.update_salary(emp_id, hours_val, rate_val)

        elif choice == '3':
            payroll.generate_payslips()

        elif choice == '4':
            print("\nEmployees with Overtime:")
            for emp in payroll.overtime_employees():
                print(f"  - {emp.name} (ID: {emp.emp_id}), Hours: {emp.hours}")

        elif choice == '5':
            payroll.export_to_csv()

        elif choice == '6':
            password = input("Enter admin password: ").strip()
            payroll.login_admin(password)

        elif choice == '7':
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, please select from the menu.")

if __name__ == "__main__":
    main()
