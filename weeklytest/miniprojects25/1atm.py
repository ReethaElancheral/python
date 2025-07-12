# 1. ATM Machine Simulation

# Concepts: while, functions, list (transaction history), string (messages).
# Login with 3 attempts using a while loop.
# Menu-driven system: balance inquiry, deposit, withdraw.
# Maintain transaction history in a list.
# Validate input strings and convert appropriately.


correct_pin = "1234"
balance = 1000.0
transaction_history = []

def display_menu():
    print("\n=== ATM MENU ===")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")


def check_balance():
    print(f"Your current balance is: ₹{balance:.2f}")


def deposit():
    global balance
    amount = input("Enter amount to deposit: ")
    if amount.replace('.', '', 1).isdigit():
        amount = float(amount)
        balance += amount
        transaction_history.append(f"Deposited: ₹{amount:.2f}")
        print(f"₹{amount:.2f} deposited successfully.")
    else:
        print("Invalid amount. Please enter a number.")


def withdraw():
    global balance
    amount = input("Enter amount to withdraw: ")
    if amount.replace('.', '', 1).isdigit():
        amount = float(amount)
        if amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdrew: ₹{amount:.2f}")
            print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid amount. Please enter a number.")


def show_history():
    if not transaction_history:
        print("No transactions yet.")
    else:
        print("\n=== Transaction History ===")
        for item in transaction_history:
            print(item)


attempts = 3
while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("Login successful.\n")
       
        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                check_balance()
            elif choice == "2":
                deposit()
            elif choice == "3":
                withdraw()
            elif choice == "4":
                show_history()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select from 1 to 5.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempt(s) remaining.")
        if attempts == 0:
            print("Account locked. Please contact your bank.")
