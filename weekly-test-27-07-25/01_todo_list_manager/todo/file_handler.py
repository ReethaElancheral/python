import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(task_list):
    with open(FILENAME, "w") as file:
        json.dump(task_list, file, indent=4)
