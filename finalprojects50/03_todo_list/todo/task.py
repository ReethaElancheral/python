# todo/task.py

from datetime import datetime

class Task:
    def __init__(self, name, deadline, status=False):
        self.name = name
        # deadline is stored as an immutable tuple (year, month, day)
        try:
            dt = datetime.strptime(deadline, "%Y-%m-%d")
            self.deadline = (dt.year, dt.month, dt.day)
        except ValueError:
            raise ValueError("Deadline must be in YYYY-MM-DD format.")
        self.status = status  # False means incomplete, True means complete

    def is_overdue(self):
        today = datetime.today().date()
        deadline_date = datetime(*self.deadline).date()
        return not self.status and deadline_date < today

    def __str__(self):
        status_str = "✓ Completed" if self.status else "✗ Pending"
        deadline_str = f"{self.deadline[0]:04d}-{self.deadline[1]:02d}-{self.deadline[2]:02d}"
        overdue_str = " [OVERDUE]" if self.is_overdue() else ""
        return f"Task: {self.name}\nDeadline: {deadline_str}{overdue_str}\nStatus: {status_str}"
