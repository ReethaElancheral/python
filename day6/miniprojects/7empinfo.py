# 🧩 7. Employee Info Manager

# Topics Covered: **kwargs, function return, dictionary
# Requirements:
# Accept name, role, salary using **kwargs
# Display formatted info using f-string
# Return dictionary of all employees


employee_db = {}

def add_employee(**kwargs):
    name = kwargs.get('name')
    role = kwargs.get('role')
    salary = kwargs.get('salary')

    if name and role and salary:
      
        employee_db[name] = {
            "Role": role,
            "Salary": salary
        }
        print(f"✅ Employee Added: {name} | Role: {role} | Salary: ₹{salary}")
    else:
        print("⚠️ Missing information. Please provide name, role, and salary.")

    return employee_db

add_employee(name="Arun", role="Developer", salary=50000)
add_employee(name="Divya", role="Manager", salary=65000)

print("\n📋 All Employees:")
print(employee_db)
