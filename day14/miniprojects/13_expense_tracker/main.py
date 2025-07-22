from expenses.tracker import add_expense, generate_summary
from expenses.display import show_banner

def main():
    show_banner()
    while True:
        print("\n1. Add Expense")
        print("2. Generate Monthly Summary")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            generate_summary()
        elif choice == "3":
            print("👋 Exiting Expense Tracker.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
