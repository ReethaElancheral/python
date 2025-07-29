# tracker/manager.py

import csv
from datetime import datetime
from tracker.expense import Expense
from tracker.utils import validate_input

class ExpenseManager:
    def __init__(self, filename="expenses.csv"):
        self.expenses = []
        self.filename = filename
        self.load_expenses()

    @validate_input
    def add_expense(self, amount, category, date):
        expense = Expense(amount, category, date)
        self.expenses.append(expense)
        print("✅ Expense added successfully.")

    def view_all_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
            return
        for e in self.expenses:
            print(e)

    def view_by_category(self, category):
        found = [e for e in self.expenses if e.category.lower() == category.lower()]
        for e in found:
            print(e)
        if not found:
            print("No expenses found in this category.")

    def view_by_month(self, year, month):
        for e in self.expenses:
            if e.date.year == int(year) and e.date.month == int(month):
                print(e)

    def filter_by_amount(self, threshold):
        for e in self.expenses:
            if e.amount > threshold:
                print(e)

    def unique_categories(self):
        return set(e.category for e in self.expenses)

    def expenses_in_date_range(self, start_date, end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        for e in self.expenses:
            if start <= e.date <= end:
                yield e

    def save_expenses(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["amount", "category", "date"])
            writer.writeheader()
            for e in self.expenses:
                writer.writerow(e.to_dict())

    def load_expenses(self):
        try:
            with open(self.filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.expenses.append(Expense.from_dict(row))
        except FileNotFoundError:
            self.expenses = []
