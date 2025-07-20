def add_expense(expenses, date, category, amount):
    expenses.append((date, category, amount))
    print(f"Added: {category} - ₹{amount} on {date}")

def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    for date, category, amount in expenses:
        print(f"{date} | {category} | ₹{amount}")
