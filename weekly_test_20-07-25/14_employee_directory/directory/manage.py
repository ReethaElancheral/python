def add_employee(employee_list, employee):
    employee_list.append(employee)
    print(f"Added: {employee['name']}")

def remove_employee(employee_list, emp_id):
    for emp in employee_list:
        if emp["id"][0] == emp_id:
            employee_list.remove(emp)
            print(f"Removed: {emp['name']}")
            return
    print("Employee not found.")

def update_employee(employee_list, emp_id, updates):
    for emp in employee_list:
        if emp["id"][0] == emp_id:
            emp.update(updates)
            print(f"Updated: {emp['name']}")
            return
    print("Employee not found.")
