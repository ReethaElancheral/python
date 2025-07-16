# 3. Employee Directory System

# Description: Maintain employee records.
# Requirements:
# - Use nested dictionary: {emp_id: {"name": ..., "dept": ..., "salary": ...}}
# - Add new employee
# - Update salary or department
# - Delete employee using pop()
# - Search employees by department
# - Use setdefault() to prevent overwriting existing records


directory = {}

def add_employee(emp_id, name, dept, salary):
 
    directory.setdefault(emp_id, {"name": name, "dept": dept, "salary": salary})

def update_employee(emp_id, dept=None, salary=None):
    if emp_id in directory:
        if dept:
            directory[emp_id]["dept"] = dept
        if salary is not None:
            directory[emp_id]["salary"] = salary

def remove_employee(emp_id):
    return directory.pop(emp_id, None)

def search_by_dept(dept):
    return {eid: info for eid, info in directory.items() if info["dept"] == dept}


add_employee(101, "Alice", "HR", 70000)
add_employee(102, "Bob", "Engineering", 90000)
add_employee(103, "Cara", "Marketing", 65000)

update_employee(102, salary=95000)
add_employee(102, "Bob", "Finance", 90000)  

removed = remove_employee(103)

engineers = search_by_dept("Engineering")


print("📂 Employee Directory:")
for eid, info in directory.items():
    print(f"ID: {eid} | Name: {info['name']} | Dept: {info['dept']} | Salary: ₹{info['salary']:.2f}")

print("\n🔍 Engineers:", engineers)
print("🗑️ Removed Employee:", removed)
