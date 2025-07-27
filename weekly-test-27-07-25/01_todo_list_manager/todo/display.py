def show_tasks(task_list):
    if not task_list:
        print("No tasks found.")
        return
    for i, task in enumerate(task_list, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']} | Done: {status}")
