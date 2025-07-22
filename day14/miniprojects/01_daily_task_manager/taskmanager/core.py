import os
from datetime import date

def get_filename():
    return date.today().strftime("%Y-%m-%d") + ".txt"

def add_task(task):
    filename = get_filename()
    with open(filename, "a") as file:
        file.write(task + "\n")
    print("Task added.")

def get_tasks():
    filename = get_filename()
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def delete_task(index):
    tasks = get_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        filename = get_filename()
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Task deleted.")
    else:
        print("Invalid task number.")
