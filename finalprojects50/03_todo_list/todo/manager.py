# todo/manager.py

from todo.task import Task
from todo.utils import timeit
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    @timeit
    def add_task(self, name, deadline):
        task = Task(name, deadline)
        self.tasks.append(task)
        print("✅ Task added.")

    @timeit
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = True
            print("✅ Task marked as completed.")
        else:
            print("Invalid task index.")

    @timeit
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"✅ Task '{removed.name}' deleted.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks):
            print(f"[{i}] {task}\n{'-'*30}")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                line = f"{task.name}|{task.deadline[0]}-{task.deadline[1]}-{task.deadline[2]}|{task.status}\n"
                f.write(line)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                self.tasks.clear()
                for line in f:
                    name, deadline_str, status_str = line.strip().split("|")
                    status = status_str == "True"
                    task = Task(name, deadline_str, status)
                    self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []
        except Exception as e:
            print(f"Failed to load tasks: {e}")

    def __iter__(self):
        # Iterator over pending tasks only
        self._iter_index = 0
        return self

    def __next__(self):
        while self._iter_index < len(self.tasks):
            task = self.tasks[self._iter_index]
            self._iter_index += 1
            if not task.status:
                return task
        raise StopIteration

    def tasks_due_today(self):
        today_str = datetime.today().strftime("%Y-%m-%d")
        for task in self.tasks:
            deadline_str = f"{task.deadline[0]:04d}-{task.deadline[1]:02d}-{task.deadline[2]:02d}"
            if deadline_str == today_str:
                yield task
