from tracker.core import add_expense, list_expenses
from tracker.summary import category_summary, monthly_summary, unique_categories
from tracker.validator import validate_date, validate_amount

expenses = []

def main():
    while True:
        print("\n1. Add Expense  2. View All  3. Summary by Category  4. Monthly Summary  5. Unique Categories  6. Exit")
        choice = input("Select: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date format.")
                continue
            category = input("Category: ").strip().capitalize()
            amount_str = input("Amount (INR): ")
            amount = validate_amount(amount_str)
            if amount is None:
                print("Invalid amount.")
                continue

            add_expense(expenses, date, category, amount)

        elif choice == "2":
            list_expenses(expenses)

        elif choice == "3":
            category_summary(expenses)

        elif choice == "4":
            monthly_summary(expenses)

        elif choice == "5":
            print("Unique Categories:", unique_categories(expenses))

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
