# 7. Employee Management System

# Description: Store employee records using nested lists.
# Add, update, remove employee.
# Access employee by index.
# Sort employees alphabetically.


employees = [
    ["Geetha", "Manager"],
    ["Reetha", "Junior Developer"],
    ["Karthiga", "Developer"]
]

def show_employees():
    if not employees:
        print("📂 No employee records.")
    else:
        print("\n👥 Employee Records:")
        for i, emp in enumerate(employees, 0):
            print(f"{i}. Name: {emp[0]}, Position: {emp[1]}")

def add_employee():
    name = input("Enter employee name: ").strip()
    position = input("Enter position: ").strip()
    employees.append([name, position])
    print(f"✅ '{name}' added as {position}.")

def update_employee():
    show_employees()
    try:
        index = int(input("Enter index of employee to update: "))
        if 0 <= index < len(employees):
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_position = input("Enter new position (leave blank to keep current): ").strip()

            if new_name:
                employees[index][0] = new_name
            if new_position:
                employees[index][1] = new_position

            print("✅ Employee record updated.")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ Enter a valid number.")

def remove_employee():
    show_employees()
    try:
        index = int(input("Enter index of employee to remove: "))
        if 0 <= index < len(employees):
            removed = employees.pop(index)
            print(f"🗑️ '{removed[0]}' removed from records.")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ Enter a valid number.")

def sort_employees():
    employees.sort(key=lambda emp: emp[0].lower()) 
    print("📊 Employees sorted alphabetically by name.")


while True:
    print("\n--- Employee Management Menu ---")
    print("1. View All Employees")
    print("2. Add Employee")
    print("3. Update Employee")
    print("4. Remove Employee")
    print("5. Sort by Name")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    if choice == "1":
        show_employees()
    elif choice == "2":
        add_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        remove_employee()
    elif choice == "5":
        sort_employees()
    elif choice == "6":
        print("👋 Exiting Employee Management System.")
        break
    else:
        print("❌ Invalid option. Please choose between 1–6.")
