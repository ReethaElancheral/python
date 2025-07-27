from todo.task_manager import (
    add_task, delete_task, mark_task_complete, search_tasks, sort_tasks
)
from todo.file_handler import load_tasks, save_tasks
from todo.display import show_tasks

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Search Tasks")
        print("6. Sort by Priority")
        print("7. Sort by Due Date")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            title = input("Enter task title: ")
            priority = input("Priority (High/Medium/Low): ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            add_task(tasks, title, priority, due_date)
            save_tasks(tasks)

        elif choice == "3":
            title = input("Enter task title to delete: ")
            delete_task(tasks, title)
            save_tasks(tasks)

        elif choice == "4":
            title = input("Enter task title to mark complete: ")
            mark_task_complete(tasks, title)
            save_tasks(tasks)

        elif choice == "5":
            keyword = input("Search keyword: ")
            results = search_tasks(tasks, keyword)
            show_tasks(results)

        elif choice == "6":
            sorted_tasks = sort_tasks(tasks, by="priority")
            show_tasks(sorted_tasks)

        elif choice == "7":
            sorted_tasks = sort_tasks(tasks, by="due_date")
            show_tasks(sorted_tasks)

        elif choice == "8":
            print("Saving and exiting...")
            save_tasks(tasks)
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
