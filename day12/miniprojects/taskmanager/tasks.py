# taskmanager/tasks.py
import json
from datetime import datetime
from pathlib import Path

TASK_FILE = Path(__file__).parent / "data" / "tasks.json"

def load_tasks():
    try:
        data = json.loads(TASK_FILE.read_text())
    except FileNotFoundError:
        data = {}
    # convert dates from string to datetime
    tasks = {}
    for tid, t in data.items():
        t["due"] = datetime.fromisoformat(t["due"])
        tasks[tid] = t
    return tasks

def save_tasks(tasks):
    data = {}
    for tid, t in tasks.items():
        data[tid] = {
            "title": t["title"],
            "due": t["due"].isoformat(),
            "priority": t["priority"]
        }
    TASK_FILE.parent.mkdir(exist_ok=True)
    TASK_FILE.write_text(json.dumps(data, indent=2))

def add_task(task_id, title, due, priority):
    tasks = load_tasks()
    tasks[task_id] = {"title": title, "due": due, "priority": priority}
    save_tasks(tasks)

def update_task(task_id, **kwargs):
    tasks = load_tasks()
    t = tasks.get(task_id)
    if not t:
        raise KeyError("No such task")
    if "title" in kwargs:
        t['title'] = kwargs['title']
    if "due" in kwargs:
        t['due'] = kwargs['due']
    if "priority" in kwargs:
        t['priority'] = kwargs['priority']
    save_tasks(tasks)

def delete_task(task_id):
    tasks = load_tasks()
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
    else:
        raise KeyError("No such task")

def list_tasks():
    return load_tasks()
