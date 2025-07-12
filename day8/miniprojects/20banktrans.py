# 20. Bank Transaction Logger

# Description: Track credits and debits.
# Store transactions in a list.
# Calculate current balance (sum).
# Slice to show last 3 transactions.
# Remove incorrect transaction.


transactions = []

def show_transactions():
    if not transactions:
        print("No transactions recorded.")
    else:
        print("\n💳 All Transactions:")
        for i, t in enumerate(transactions, 1):
            type_tx = "Credit" if t > 0 else "Debit"
            print(f"{i}. {type_tx}: ₹{abs(t)}")

def add_transaction():
    amount = input("Enter transaction amount (positive for credit, negative for debit): ").strip()
    try:
        amt = float(amount)
        transactions.append(amt)
        print(f"Transaction of ₹{amt} added.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def remove_transaction():
    show_transactions()
    if not transactions:
        return
    index = input("Enter transaction number to remove: ")
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            print(f"Removed transaction: ₹{removed}")
        else:
            print("Invalid transaction number.")
    else:
        print("Enter a valid number.")

def show_last_three():
    print("\n📋 Last 3 Transactions:")
    last_three = transactions[-3:]
    if not last_three:
        print("No transactions to show.")
    else:
        for t in last_three:
            type_tx = "Credit" if t > 0 else "Debit"
            print(f"{type_tx}: ₹{abs(t)}")

def calculate_balance():
    balance = sum(transactions)
    print(f"\n💰 Current Balance: ₹{balance:.2f}")


while True:
    print("\n--- Bank Transaction Logger ---")
    print("1. Show All Transactions")
    print("2. Add Transaction")
    print("3. Remove Transaction")
    print("4. Show Last 3 Transactions")
    print("5. Show Current Balance")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_transactions()
    elif choice == "2":
        add_transaction()
    elif choice == "3":
        remove_transaction()
    elif choice == "4":
        show_last_three()
    elif choice == "5":
        calculate_balance()
    elif choice == "6":
        print("Exiting Transaction Logger. Goodbye!")
        break
    else:
        print("Invalid choice.")
