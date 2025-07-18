

def calculate_tax(employee):
    gross_salary = employee['base_salary']
    if gross_salary <= 25000:
        return gross_salary * 0.05
    elif gross_salary <= 50000:
        return gross_salary * 0.1
    else:
        return gross_salary * 0.15
