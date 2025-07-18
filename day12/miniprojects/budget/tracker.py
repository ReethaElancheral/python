# budget/tracker.py

import csv
from datetime import datetime

EXPENSE_FILE = 'expenses.csv'

def add_expense(category: str, amount: float, date: str = None):
    date = date or datetime.now().strftime('%Y-%m-%d')
    with open(EXPENSE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, f"{amount:.2f}"])
    return date, category, amount
