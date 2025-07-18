

def calculate_gross_salary(employee):
    return employee['base_salary']

def calculate_net_salary(employee, deductions):
    return calculate_gross_salary(employee) - deductions
