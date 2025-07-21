# 17. ATM Machine Simulation

# Concepts: Encapsulation, Static Method, Overloading
# Classes:  ATM, Account, Transaction
# Requirements:
# Withdraw, deposit, balance enquiry
# Use private balance, secure PIN
# Overload withdraw() with *args

class Account:
    def __init__(self, acc_number, owner, pin, balance=0):
        self.acc_number = acc_number
        self.owner = owner
        self.__pin = pin               # private PIN
        self.__balance = balance       # private balance

    def check_pin(self, pin):
        return self.__pin == pin

    def get_balance(self, pin):
        if self.check_pin(pin):
            return self.__balance
        else:
            print("Incorrect PIN!")
            return None

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, pin, *args):
        if not self.check_pin(pin):
            print("Incorrect PIN!")
            return

        if len(args) == 1:
            amount = args[0]
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            if amount > self.__balance:
                print("Insufficient balance.")
                return
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully. New balance: ₹{self.__balance}")

        elif len(args) > 1:
            total_amount = sum(args)
            if total_amount <= 0:
                print("Withdrawal amounts must be positive.")
                return
            if total_amount > self.__balance:
                print("Insufficient balance for combined withdrawal.")
                return
            self.__balance -= total_amount
            print(f"₹{total_amount} withdrawn successfully in multiple transactions. New balance: ₹{self.__balance}")
        else:
            print("No amount specified for withdrawal.")

class Transaction:
    @staticmethod
    def print_receipt(account, transaction_type, amount):
        print(f"Transaction Receipt:\nAccount: {account.acc_number}\nType: {transaction_type}\nAmount: ₹{amount}")

class ATM:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        self.account.deposit(amount)
        Transaction.print_receipt(self.account, "Deposit", amount)

    def withdraw(self, pin, *args):
        # Supports overloading: single or multiple withdrawal amounts
        self.account.withdraw(pin, *args)
        total = sum(args) if args else 0
        if total > 0:
            Transaction.print_receipt(self.account, "Withdrawal", total)

    def balance_enquiry(self, pin):
        balance = self.account.get_balance(pin)
        if balance is not None:
            print(f"Current balance: ₹{balance}")

def main():
    acc = Account("ACC123", "Nisha", pin="4321", balance=10000)
    atm = ATM(acc)

    # Deposit money
    atm.deposit(2000)

    # Withdraw single amount
    atm.withdraw("4321", 3000)

    # Withdraw multiple amounts
    atm.withdraw("4321", 1000, 500, 700)

    # Balance enquiry
    atm.balance_enquiry("4321")

    # Incorrect PIN usage
    atm.withdraw("0000", 100)

if __name__ == "__main__":
    main()
