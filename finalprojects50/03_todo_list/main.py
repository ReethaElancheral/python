# main.py

from todo.manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n📝 To-Do List with Reminders")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. View Pending Tasks")
        print("6. Tasks Due Today")
        print("7. Save & Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Task name: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            try:
                manager.add_task(name, deadline)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            manager.display_tasks()
            try:
                index = int(input("Enter task index to complete: "))
                manager.complete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            manager.display_tasks()
            try:
                index = int(input("Enter task index to delete: "))
                manager.delete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            manager.display_tasks()

        elif choice == "5":
            print("Pending Tasks:")
            for task in manager:
                print(task)
                print("-"*30)

        elif choice == "6":
            print("Tasks due today:")
            any_due = False
            for task in manager.tasks_due_today():
                print(task)
                print("-"*30)
                any_due = True
            if not any_due:
                print("No tasks due today.")

        elif choice == "7":
            manager.save_tasks()
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
