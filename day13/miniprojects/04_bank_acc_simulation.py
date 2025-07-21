# 4. Bank Account Simulation

# Concepts: Class, Inheritance, Encapsulation, Method Overriding
# Classes:  Account, SavingsAccount,  CurrentAccount,  Transaction
# Requirements:
# Create new accounts, track balance
# Withdraw, deposit, transfer funds
# Secure balance using private attributes
# Apply different withdrawal limits for account types

class Transaction:
    def __init__(self, transaction_type, amount, description=""):
        self.transaction_type = transaction_type 
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.transaction_type.title()}: ₹{self.amount} {self.description}"


class Account:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.__balance = 0  # private attribute
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(Transaction("deposit", amount))
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False
        if amount > self.__balance:
            print("Insufficient balance.")
            return False
        self.__balance -= amount
        self.transactions.append(Transaction("withdraw", amount))
        print(f"₹{amount} withdrawn successfully.")
        return True

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            self.transactions.append(Transaction("transfer", amount, f"to {target_account.account_number}"))
            print(f"Transferred ₹{amount} to account {target_account.account_number}.")
            return True
        return False

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account {self.account_number} owned by {self.owner}, Balance: ₹{self.__balance}"

    def print_transactions(self):
        print(f"Transactions for account {self.account_number}:")
        if not self.transactions:
            print("No transactions yet.")
        for t in self.transactions:
            print(t)


class SavingsAccount(Account):
    WITHDRAWAL_LIMIT = 50000

    def withdraw(self, amount):
        if amount > SavingsAccount.WITHDRAWAL_LIMIT:
            print(f"Cannot withdraw more than ₹{SavingsAccount.WITHDRAWAL_LIMIT} in one transaction.")
            return False
        return super().withdraw(amount)


class CurrentAccount(Account):
    WITHDRAWAL_LIMIT = 100000

    def withdraw(self, amount):
        if amount > CurrentAccount.WITHDRAWAL_LIMIT:
            print(f"Cannot withdraw more than ₹{CurrentAccount.WITHDRAWAL_LIMIT} in one transaction.")
            return False
        return super().withdraw(amount)


def main():
    # Create accounts
    sav_acc = SavingsAccount("SA123", "Nisha")
    curr_acc = CurrentAccount("CA456", "Rajesh")

    # Deposit money
    sav_acc.deposit(60000)
    curr_acc.deposit(150000)

    # Withdraw money
    sav_acc.withdraw(60000)  # Should be allowed (limit 50000) - will fail
    sav_acc.withdraw(40000)  # Allowed
    curr_acc.withdraw(120000)  # Exceeds limit - fail
    curr_acc.withdraw(90000)   # Allowed

    # Transfer money
    curr_acc.transfer(sav_acc, 30000)

    # Print balances
    print(sav_acc)
    print(curr_acc)

    # Print transactions
    sav_acc.print_transactions()
    curr_acc.print_transactions()


if __name__ == "__main__":
    main()
