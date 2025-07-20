def search_by_name(employee_list, name):
    for emp in employee_list:
        if name.lower() in emp["name"].lower():
            print(emp)

def search_by_department(employee_list, department):
    for emp in employee_list:
        if emp["department"].lower() == department.lower():
            print(emp)
