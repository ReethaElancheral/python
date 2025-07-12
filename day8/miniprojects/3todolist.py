# 3. To-Do List Manager

# Description: Create a CLI-based daily planner.
# Store tasks in a list.
# Mark tasks as complete (use remove() or pop()).
# Use slicing to show top priority tasks.
# Loop through and print tasks with index using enumerate().



tasks = []

def show_tasks():
    if not tasks:
        print("✅ No tasks in your list!")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def mark_complete():
    show_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"✅ '{removed}' marked as complete and removed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def show_top_priority():
    print("\n🔝 Top Priority Tasks:")
    if len(tasks) >= 3:
        print(tasks[:3])  
    else:
        print(tasks) 


while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Show Top Priority Tasks")
    print("5. Exit")

    choice = input("Choose an option (1–5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        show_top_priority()
    elif choice == "5":
        print("🛑 Exiting To-Do List. Have a productive day!")
        break
    else:
        print("Invalid option. Please choose between 1–5.")
