# budget/planner.py

import csv
from datetime import datetime

BUDGET_FILE = 'budgets.csv'

def set_budget(category: str, amount: float, month: str = None):
    month = month or datetime.now().strftime('%Y-%m')
    with open(BUDGET_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([month, category, f"{amount:.2f}"])
    return month, category, amount
