# 7. ATM 

# Use Case: Simulate withdrawal, deposit, balance check. 
# Exception Handling Goals:
# Raise InsufficientFundsError if withdrawal > balance
# Catch non-numeric input
# Use nested try for each transaction
# Use assert to validate positive amounts

# Custom Exception
class InsufficientFundsError(Exception):
    pass

class ATM:
    def __init__(self, balance=10000):
        self.balance = balance

    def deposit(self, amount):
        try:
            assert amount > 0, "Deposit amount must be positive"
            self.balance += amount
            print(f"✅ ₹{amount:.2f} deposited. New Balance: ₹{self.balance:.2f}")
        except AssertionError as ae:
            print(f"❌ {ae}")

    def withdraw(self, amount):
        try:
            assert amount > 0, "Withdrawal amount must be positive"
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient balance for this withdrawal.")
            self.balance -= amount
            print(f"✅ ₹{amount:.2f} withdrawn. New Balance: ₹{self.balance:.2f}")
        except AssertionError as ae:
            print(f"❌ {ae}")
        except InsufficientFundsError as ie:
            print(f"❌ {ie}")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance:.2f}")

def main():
    atm = ATM()

    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                atm.check_balance()

            elif choice == 2:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    atm.deposit(amount)
                except ValueError:
                    print("❌ Invalid input. Enter a valid number.")

            elif choice == 3:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    atm.withdraw(amount)
                except ValueError:
                    print("❌ Invalid input. Enter a valid number.")

            elif choice == 4:
                print("👋 Thank you for using the ATM!")
                break

            else:
                print("❌ Invalid choice. Please choose 1–4.")

        except ValueError:
            print("❌ Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
