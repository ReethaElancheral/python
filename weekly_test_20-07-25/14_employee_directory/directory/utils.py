def list_departments(employee_list):
    return set(emp["department"] for emp in employee_list)
