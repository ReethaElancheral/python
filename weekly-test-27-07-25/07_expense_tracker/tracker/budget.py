from datetime import datetime

monthly_budgets = {}  

def set_monthly_budget(month_str, amount):
    monthly_budgets[month_str] = amount

def get_monthly_budget(month_str):
    return monthly_budgets.get(month_str, 0)

def is_over_budget(month_str, total_spent):
    budget = get_monthly_budget(month_str)
    return total_spent > budget
