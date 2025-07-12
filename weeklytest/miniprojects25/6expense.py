# 6. Expense Tracker with Categories

# Concepts: list, string formatting, functions, while.
# User enters expenses (amount + category).
# Store in list of dicts or nested lists.
# Show total, category-wise total using functions.
# Menu-driven loop.



expenses = []  


def add_expense():
    amt = input("Enter expense amount: ").strip()
    cat = input("Enter category (e.g. food, transport, etc.): ").strip().lower()
    
    if amt.replace('.', '', 1).isdigit() and cat:
        amt = float(amt)
        expenses.append({"amount": amt, "category": cat})
        print(f"Added: ₹{amt:.2f} in '{cat}' category.")
    else:
        print("Invalid input. Amount must be a number, and category cannot be empty.")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n=== All Expenses ===")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']:.2f} - {exp['category']}")
    print()


def total_spent():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spent: ₹{total:.2f}")


def category_totals():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n=== Category Totals ===")
    categories = {}
    for exp in expenses:
        cat = exp["category"]
        categories[cat] = categories.get(cat, 0) + exp["amount"]

    for cat, amt in categories.items():
        print(f"{cat.capitalize()}: ₹{amt:.2f}")
    print()


while True:
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Total Spent")
    print("4. Show Category-wise Totals")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        category_totals()
    elif choice == "5":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 5.")
