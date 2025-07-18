# budget/report.py

import csv
from datetime import datetime
from math import ceil
from tabulate import tabulate

from .planner import BUDGET_FILE
from .tracker import EXPENSE_FILE

def monthly_report(month: str = None):
    month = month or datetime.now().strftime('%Y-%m')

    budgets = {}
    try:
        with open(BUDGET_FILE) as f:
            for m, cat, amt in csv.reader(f):
                if m == month:
                    budgets[cat] = budgets.get(cat, 0) + float(amt)
    except FileNotFoundError:
        pass

    expenses = {}
    try:
        with open(EXPENSE_FILE) as f:
            for date, cat, amt in csv.reader(f):
                if date.startswith(month):
                    expenses[cat] = expenses.get(cat, 0) + float(amt)
    except FileNotFoundError:
        pass

    categories = sorted(set(budgets) | set(expenses))
    rows = []
    for cat in categories:
        b = budgets.get(cat, 0)
        e = expenses.get(cat, 0)
        diff = b - e
        pct = (e / b * 100) if b > 0 else None
        rows.append([cat, b, e, diff, f"{pct:.1f}%" if pct is not None else 'N/A'])

    headers = ['Category', 'Budgeted', 'Spent', 'Remaining', '% Used']
    table = tabulate(rows, headers, floatfmt=".2f", tablefmt="grid")
    return table
