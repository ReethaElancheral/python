from datetime import datetime

tasks = []

def add_task(title, due_date, priority, tags, notes):
    task = {
        'info': (title, due_date),  
        'priority': priority,
        'tags': set(tags),
        'notes': notes,
        'completed': False
    }
    tasks.append(task)

def complete_task(title):
    for task in tasks:
        if task['info'][0] == title:
            task['completed'] = True
            return True
    return False

def delete_task(title):
    global tasks
    tasks = [task for task in tasks if task['info'][0] != title]

def get_overdue_tasks():
    today = datetime.today().date()
    return [task for task in tasks if datetime.strptime(task['info'][1], "%Y-%m-%d").date() < today and not task['completed']]

def group_by_priority():
    priority_dict = {}
    for task in tasks:
        priority_dict.setdefault(task['priority'], []).append(task)
    return priority_dict

def list_all_tasks():
    return tasks
