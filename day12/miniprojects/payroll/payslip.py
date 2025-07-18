

from datetime import datetime
from payroll.salary import calculate_net_salary
from payroll.tax import calculate_tax

def generate_payslip(employee, deductions):
    net_salary = calculate_net_salary(employee, deductions)
    tax = calculate_tax(employee)
    payslip = f"""
    Payslip for {employee['name']}
    Date: {datetime.now().strftime('%Y-%m-%d')}
    ----------------------------------------
    Gross Salary: {employee['base_salary']}
    Tax Deduction: {tax}
    Deductions: {deductions}
    Net Salary: {net_salary}
    """
    return payslip
