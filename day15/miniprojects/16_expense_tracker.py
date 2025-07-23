# 16. Expense Tracker App

# Use Case: Track and categorize expenses. 
# Exception Handling Goals:
# Raise InvalidCategoryError
# Catch non-numeric expense entries
# Use try-except-finally to always show total

# Custom Exception
class InvalidCategoryError(Exception):
    pass

def expense_tracker():
    allowed_categories = ['food', 'travel', 'shopping', 'bills', 'others']
    expenses = {}
    total_expense = 0

    while True:
        try:
            category = input("Enter expense category (food/travel/shopping/bills/others) or 'done' to finish: ").strip().lower()
            if category == 'done':
                break

            if category not in allowed_categories:
                raise InvalidCategoryError(f"Category '{category}' is not valid.")

            amount_input = input(f"Enter amount for {category}: ₹")
            amount = float(amount_input)
            if amount < 0:
                raise ValueError("Expense amount cannot be negative.")

            expenses[category] = expenses.get(category, 0) + amount

        except InvalidCategoryError as ice:
            print(f"❌ {ice}")
        except ValueError as ve:
            print(f"❌ Invalid amount: {ve}")
        finally:
            total_expense = sum(expenses.values())
            print(f"💰 Total expenses so far: ₹{total_expense:.2f}\n")

    print("\n📝 Expense summary:")
    for cat, amt in expenses.items():
        print(f"  {cat.capitalize()}: ₹{amt:.2f}")
    print(f"💰 Total expense: ₹{total_expense:.2f}")

if __name__ == "__main__":
    expense_tracker()
