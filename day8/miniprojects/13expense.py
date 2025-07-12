# 13. Budget Expense Tracker

# Description: Track user expenses using a list.
# Add new expenses.
# Update old ones.
# Show last 3 expenses (slicing).
# Remove wrong entries.



expenses = []

def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\n💸 All Expenses:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. ₹{expense}")

def add_expense():
    amount = input("Enter expense amount: ").strip()
    if amount.isdigit():
        expenses.append(int(amount))
        print(f"₹{amount} added to expenses.")
    else:
        print("Invalid amount. Please enter a number.")

def update_expense():
    show_expenses()
    if not expenses:
        return
    index = input("Enter expense number to update: ")
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(expenses):
            new_amount = input("Enter new amount: ").strip()
            if new_amount.isdigit():
                old = expenses[index]
                expenses[index] = int(new_amount)
                print(f"Expense {old} updated to {new_amount}.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid expense number.")
    else:
        print("Enter a valid number.")

def remove_expense():
    show_expenses()
    if not expenses:
        return
    index = input("Enter expense number to remove: ")
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(f"Removed expense ₹{removed}.")
        else:
            print("Invalid expense number.")
    else:
        print("Enter a valid number.")

def show_last_three():
    print("\n📋 Last 3 expenses:")
    if len(expenses) < 3:
        for expense in expenses:
            print(f"₹{expense}")
    else:
        for expense in expenses[-3:]:
            print(f"₹{expense}")


while True:
    print("\n--- Budget Expense Tracker ---")
    print("1. Show All Expenses")
    print("2. Add Expense")
    print("3. Update Expense")
    print("4. Remove Expense")
    print("5. Show Last 3 Expenses")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_expenses()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        remove_expense()
    elif choice == "5":
        show_last_three()
    elif choice == "6":
        print("Exiting Expense Tracker. Bye!")
        break
    else:
        print("Invalid choice.")
