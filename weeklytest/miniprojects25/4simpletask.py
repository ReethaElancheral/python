# Simple Task Manager

# Concepts: while menu loop, string operations, lists.
# Tasks stored in a list.
# Add, delete, mark complete using menu options.
# Display using formatted string output.
# Use functions for modularity.


tasks = []  

def add_task():
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    display_tasks()
    index = input("Enter task number to delete: ").strip()
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

def mark_complete():
    if not tasks:
        print("No tasks to mark.")
        return

    display_tasks()
    index = input("Enter task number to mark complete: ").strip()
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print(f"Marked as complete: {tasks[index]['title']}")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n=== Task List ===")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['title']} [{status}]")
        print()


while True:
    print("\n=== Task Manager Menu ===")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Complete")
    print("4. Show All Tasks")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 5.")
