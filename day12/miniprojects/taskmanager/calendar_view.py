# taskmanager/calendar_view.py

import calendar
from datetime import datetime
from .tasks import load_tasks

def tasks_by_month(year, month):
    tasks = load_tasks()
    result = {}
    for t in tasks.values():
        if t['due'].year == year and t['due'].month == month:
            day = t['due'].day
            result.setdefault(day, []).append(t)
    return result

def print_month(year, month):
    cal = calendar.TextCalendar()
    print(cal.formatmonth(year, month))
    tasks = tasks_by_month(year, month)
    for day, ts in sorted(tasks.items()):
        print(f"{year}-{month:02d}-{day:02d}:")
        for t in ts:
            print(f"  • {t['title']} (prio {t['priority']})")
