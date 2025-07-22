import csv
import os
from datetime import datetime

DATA_DIR = "expenses_data"

def get_monthly_file(date_obj):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    filename = date_obj.strftime("%Y-%m") + "_expenses.csv"
    return os.path.join(DATA_DIR, filename)

def add_expense():
    category = input("Category: ").strip()
    amount = input("Amount (₹): ").strip()
    date_str = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
    if not date_str:
        date_obj = datetime.now()
    else:
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format.")
            return
    try:
        amount_val = float(amount)
    except ValueError:
        print("❌ Invalid amount.")
        return

    filepath = get_monthly_file(date_obj)
    file_exists = os.path.exists(filepath)
    with open(filepath, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Category", "Amount", "Date"])
        writer.writerow([category, amount_val, date_obj.strftime("%Y-%m-%d")])
    print(f"✅ Expense added to {filepath}")

def generate_summary():
    month_year = input("Enter month and year (YYYY-MM): ").strip()
    try:
        date_obj = datetime.strptime(month_year, "%Y-%m")
    except ValueError:
        print("❌ Invalid month-year format.")
        return

    filepath = get_monthly_file(date_obj)
    if not os.path.exists(filepath):
        print("❌ No expense data found for this month.")
        return

    total = 0
    category_totals = {}

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row["Amount"])
            cat = row["Category"]
            total += amt
            category_totals[cat] = category_totals.get(cat, 0) + amt

    print(f"\nExpense Summary for {month_year}:")
    print(f"Total Spent: ₹{total:.2f}")
    print("By Category:")
    for cat, amt in category_totals.items():
        print(f" - {cat}: ₹{amt:.2f}")
