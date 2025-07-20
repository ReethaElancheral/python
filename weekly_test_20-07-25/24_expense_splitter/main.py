from splitter.expense_ops import add_expense, show_expenses
from splitter.balance_ops import calculate_balances, show_balances

def main():
    expenses = []
    categories = set()

    while True:
        print("\n🏠 Expense Splitter for Roommates")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Balances")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_expense(expenses, categories)
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '3':
            balances = calculate_balances(expenses)
            show_balances(balances)
        elif choice == '0':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
