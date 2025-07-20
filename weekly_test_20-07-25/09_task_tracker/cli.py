from task_ops import add_task, complete_task, delete_task, get_overdue_tasks, group_by_priority, list_all_tasks

def show_menu():
    print("\n--- Task Tracker Menu ---")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. Show Overdue Tasks")
    print("5. Group by Priority")
    print("6. List All Tasks")
    print("0. Exit")

def run():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            tags = input("Tags (comma-separated): ").split(',')
            notes = input("Notes: ")
            add_task(title, due_date, priority, tags, notes)

        elif choice == "2":
            title = input("Task to complete: ")
            if complete_task(title):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == "3":
            title = input("Task to delete: ")
            delete_task(title)
            print("Task deleted.")

        elif choice == "4":
            overdue = get_overdue_tasks()
            print(f"\nOverdue Tasks ({len(overdue)}):")
            for task in overdue:
                print(task['info'][0], "| Due:", task['info'][1])

        elif choice == "5":
            grouped = group_by_priority()
            for priority, group in grouped.items():
                print(f"\nPriority: {priority}")
                for task in group:
                    print("-", task['info'][0])

        elif choice == "6":
            for task in list_all_tasks():
                print(f"{task['info'][0]} | Due: {task['info'][1]} | Priority: {task['priority']} | Tags: {task['tags']} | Done: {task['completed']}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
