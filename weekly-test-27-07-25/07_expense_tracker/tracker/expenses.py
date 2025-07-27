import csv
import os
from datetime import datetime

DATA_FILE = "expenses.csv"
FIELDS = ["date", "category", "amount", "description"]

def add_expense(date, category, amount, description=""):
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })

def load_expenses():
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses

    with open(DATA_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            row["date"] = datetime.strptime(row["date"], "%Y-%m-%d").date()
            expenses.append(row)
    return expenses
