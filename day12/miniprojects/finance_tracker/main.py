from finance import income, expense, summary

def main():
    print("=== Personal Finance Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        amount = float(input("Enter amount: "))
        source = input("Enter income source: ")
        income.add_income(amount, source)
        print("Income added.")
    elif choice == '2':
        amount = float(input("Enter amount: "))
        category = input("Enter expense category: ")
        expense.add_expense(amount, category)
        print("Expense added.")
    elif choice == '3':
        summary.show_summary()
    elif choice == '4':
        print("Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
