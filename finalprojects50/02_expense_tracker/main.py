# main.py

# 2. Expense Tracker 
# Objective: Track daily expenses with categories. 
# Requirements: 
#  OOP: Expense class (amount, category, date). 
#  List/Dict: Store expenses in a list of dictionaries. 
#  File Handling: Save to CSV. 
#  Exception Handling: Invalid amount/date. 
#  Functions: Add expense, view by category/month. 
#  Loops: Filter expenses (e.g., "Show expenses > $100"). 
#  String Formatting: Display expenses neatly. 
#  Set: Unique expense categories. 
#  Generator: Yield expenses in a date range. 

# main.py

from tracker.manager import ExpenseManager

def main():
    manager = ExpenseManager()

    while True:
        print("\n💸 Expense Tracker CLI")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. View by Month")
        print("5. Filter Expenses > Amount")
        print("6. Unique Categories")
        print("7. Expenses in Date Range")
        print("8. Save & Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            amt = input("Amount (₹): ")
            cat = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            try:
                amt = float(amt)
                manager.add_expense(amt, cat, date)
            except ValueError:
                print("Amount must be a valid number.")

        elif choice == "2":
            manager.view_all_expenses()

        elif choice == "3":
            cat = input("Enter category: ")
            manager.view_by_category(cat)

        elif choice == "4":
            y = input("Enter year (YYYY): ")
            m = input("Enter month (1–12): ")
            manager.view_by_month(y, m)

        elif choice == "5":
            amt = input("Show expenses > ₹: ")
            try:
                amt_float = float(amt)
                manager.filter_by_amount(amt_float)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "6":
            categories = manager.unique_categories()
            if categories:
                print("Unique Categories:")
                for c in categories:
                    print(f"- {c}")
            else:
                print("No categories found.")

        elif choice == "7":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            try:
                for e in manager.expenses_in_date_range(start, end):
                    print(e)
            except ValueError:
                print("Dates must be in YYYY-MM-DD format.")

        elif choice == "8":
            manager.save_expenses()
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
