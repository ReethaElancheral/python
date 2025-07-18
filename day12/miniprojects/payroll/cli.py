
import argparse
from payroll.employee import create_employee
from payroll.salary import calculate_gross_salary, calculate_net_salary
from payroll.tax import calculate_tax
from payroll.payslip import generate_payslip

def main():
    parser = argparse.ArgumentParser(description="Employee Payroll System")
    parser.add_argument('--id', type=int, required=True, help="Employee ID")
    parser.add_argument('--name', type=str, required=True, help="Employee Name")
    parser.add_argument('--base_salary', type=float, required=True, help="Base Salary")
    parser.add_argument('--deductions', type=float, required=True, help="Total Deductions")
    args = parser.parse_args()

    employee = create_employee(args.id, args.name, args.base_salary)
    gross_salary = calculate_gross_salary(employee)
    net_salary = calculate_net_salary(employee, args.deductions)
    tax = calculate_tax(employee)
    payslip = generate_payslip(employee, args.deductions)

    print(f"Employee: {employee['name']}")
    print(f"Gross Salary: {gross_salary}")
    print(f"Net Salary: {net_salary}")
    print(f"Tax Deduction: {tax}")
    print("Payslip Generated:")
    print(payslip)

if __name__ == "__main__":
    main()
