from tracker.expenses import add_expense, load_expenses
from tracker.budget import set_monthly_budget, get_monthly_budget, is_over_budget
from tracker.reports import monthly_spending_report, category_spending_report
from tracker.visualization import plot_monthly_spending, plot_category_spending
from datetime import datetime
import csv

def export_expenses_to_csv(filename="expenses_export.csv"):
    expenses = load_expenses()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        for exp in expenses:
            exp_copy = exp.copy()
            exp_copy["date"] = exp_copy["date"].strftime("%Y-%m-%d")
            writer.writerow(exp_copy)
    print(f"Expenses exported to {filename}")

def main():
    print("Welcome to Expense Tracker!")
    expenses = load_expenses()

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Set Monthly Budget")
        print("3. View Monthly Spending Report")
        print("4. View Category Spending Report")
        print("5. Visualize Monthly Spending")
        print("6. Visualize Category Spending")
        print("7. Export Expenses to CSV")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date_str = input("Date (YYYY-MM-DD), leave blank for today: ").strip()
            if not date_str:
                date = datetime.today().date()
            else:
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format.")
                    continue
            category = input("Category (e.g., Food, Transport): ").strip()
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount.")
                continue
            description = input("Description (optional): ").strip()
            add_expense(date.strftime("%Y-%m-%d"), category, amount, description)
            print("Expense added.")

        elif choice == "2":
            month = input("Enter month (YYYY-MM): ")
            try:
                datetime.strptime(month, "%Y-%m")
            except ValueError:
                print("Invalid month format.")
                continue
            try:
                amount = float(input("Enter budget amount: "))
            except ValueError:
                print("Invalid amount.")
                continue
            set_monthly_budget(month, amount)
            print(f"Budget for {month} set to {amount}")

        elif choice == "3":
            expenses = load_expenses()
            report = monthly_spending_report(expenses)
            print("Monthly Spending Report:")
            for month, total in sorted(report.items()):
                budget = get_monthly_budget(month)
                status = "(Over Budget)" if is_over_budget(month, total) else ""
                print(f"{month}: ₹{total:.2f} Budget: ₹{budget:.2f} {status}")

        elif choice == "4":
            expenses = load_expenses()
            report = category_spending_report(expenses)
            print("Category Spending Report:")
            for cat, total in sorted(report.items()):
                print(f"{cat}: ₹{total:.2f}")

        elif choice == "5":
            expenses = load_expenses()
            report = monthly_spending_report(expenses)
            if report:
                plot_monthly_spending(report)
            else:
                print("No expenses to visualize.")

        elif choice == "6":
            expenses = load_expenses()
            report = category_spending_report(expenses)
            if report:
                plot_category_spending(report)
            else:
                print("No expenses to visualize.")

        elif choice == "7":
            export_expenses_to_csv()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
