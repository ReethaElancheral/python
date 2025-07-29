# 10. Bank Account Simulator 
# Objective: Simulate deposits, withdrawals, transfers. 
# Requirements: 
#  OOP: BankAccount class (balance, transactions). 
#  List: Store transaction history. 
#  File Handling: Save account details. 
#  Exception Handling: Insufficient balance. 
#  Functions: Deposit, withdraw, transfer. 
#  Loops: Display transaction history. 
#  Conditionals: Apply interest if balance > $1000. 
#  Generator: Yield transactions of a certain type. 
#  Decorator: @audit to log transactions.

from bank.account import BankAccount

def main():
    print("🏦 Welcome to the CLI Bank Simulator")
    user = BankAccount("Nisha")
    other = BankAccount("Reetha")  # secondary account for transfer testing

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer to Reetha")
        print("4. Show Balance")
        print("5. Show Transactions")
        print("6. Apply Interest")
        print("7. Filter Transactions")
        print("8. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            try:
                amt = float(input("Enter deposit amount: "))
                user.deposit(amt)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == '2':
            try:
                amt = float(input("Enter withdrawal amount: "))
                user.withdraw(amt)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == '3':
            try:
                amt = float(input("Enter amount to transfer to Reetha: "))
                user.transfer(other, amt)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == '4':
            user.show_balance()
        elif choice == '5':
            user.show_transactions()
        elif choice == '6':
            user.apply_interest()
            print("✅ Interest applied if balance > ₹1000.")
        elif choice == '7':
            keyword = input("Enter transaction type (e.g., deposit, withdrew, transferred): ")
            print(f"\n🔍 Matching transactions for '{keyword}':")
            for txn in user.transaction_generator(keyword):
                print("-", txn)
        elif choice == '8':
            print("👋 Exiting... Thank you for using Bank Simulator.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
