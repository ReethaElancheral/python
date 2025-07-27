import datetime

def add_task(task_list, title, priority, due_date):
    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    task_list.append(task)

def delete_task(task_list, title):
    task_list[:] = [task for task in task_list if task["title"].lower() != title.lower()]

def mark_task_complete(task_list, title):
    for task in task_list:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            break

def search_tasks(task_list, keyword):
    return [task for task in task_list if keyword.lower() in task["title"].lower()]

def sort_tasks(task_list, by="priority"):
    if by == "priority":
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        return sorted(task_list, key=lambda x: priority_order.get(x["priority"], 4))
    elif by == "due_date":
        return sorted(task_list, key=lambda x: datetime.datetime.strptime(x["due_date"], "%Y-%m-%d"))
    return task_list
