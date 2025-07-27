from collections import defaultdict
from datetime import datetime

def monthly_spending_report(expenses):
    report = defaultdict(float)
    for exp in expenses:
        month = exp["date"].strftime("%Y-%m")
        report[month] += exp["amount"]
    return dict(report)

def category_spending_report(expenses):
    report = defaultdict(float)
    for exp in expenses:
        report[exp["category"]] += exp["amount"]
    return dict(report)
