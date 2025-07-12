# 11. Simple Banking System

# Concepts: while, list (transactions), functions.
# Options: deposit, withdraw, check balance.
# Store transactions as list of strings.
# Print transaction history.

transactions = []
balance = 0.0

def deposit():
    global balance
    amt = input("Enter deposit amount: ").strip()
    if amt.replace('.', '', 1).isdigit():
        amt = float(amt)
        if amt > 0:
            balance += amt
            transactions.append(f"Deposited: ₹{amt:.2f}")
            print(f"₹{amt:.2f} deposited successfully.")
        else:
            print("Amount must be positive.")
    else:
        print("Invalid amount entered.")

def withdraw():
    global balance
    amt = input("Enter withdrawal amount: ").strip()
    if amt.replace('.', '', 1).isdigit():
        amt = float(amt)
        if amt > 0:
            if amt <= balance:
                balance -= amt
                transactions.append(f"Withdrawn: ₹{amt:.2f}")
                print(f"₹{amt:.2f} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Amount must be positive.")
    else:
        print("Invalid amount entered.")

def check_balance():
    print(f"Current balance: ₹{balance:.2f}")

def print_transactions():
    if not transactions:
        print("No transactions yet.")
    else:
        print("\n=== Transaction History ===")
        for t in transactions:
            print(t)
    print()


while True:
    print("\n=== Banking System Menu ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        print_transactions()
    elif choice == "5":
        print("Thank you for banking with us. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 5.")
