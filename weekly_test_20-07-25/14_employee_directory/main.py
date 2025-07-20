from directory.manage import add_employee, remove_employee, update_employee
from directory.search import search_by_name, search_by_department
from directory.utils import list_departments

employees = []

if __name__ == "__main__":
    emp1 = {
        "id": ("E001",),
        "name": "Alice Johnson",
        "department": "HR",
        "email": "alice@example.com"
    }

    emp2 = {
        "id": ("E002",),
        "name": "Bob Smith",
        "department": "Engineering",
        "email": "bob@example.com"
    }

    add_employee(employees, emp1)
    add_employee(employees, emp2)
    
    print("\nAll departments:")
    print(list_departments(employees))

    print("\nSearch by department:")
    search_by_department(employees, "Engineering")

    print("\nSearch by name:")
    search_by_name(employees, "Alice")

    print("\nUpdating employee email:")
    update_employee(employees, "E002", {"email": "bob.smith@example.com"})

    print("\nRemoving employee:")
    remove_employee(employees, "E001")
