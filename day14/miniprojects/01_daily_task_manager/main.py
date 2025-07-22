from taskmanager.core import add_task, delete_task, get_tasks
from taskmanager.display import show_menu

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1–4): ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            tasks = get_tasks()
            if tasks:
                print("\nToday's Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks for today.")
        elif choice == "3":
            tasks = get_tasks()
            if not tasks:
                print("No tasks to delete.")
                continue
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
