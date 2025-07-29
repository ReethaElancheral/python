import json
from bank.utils import audit

class BankAccount:
    def __init__(self, owner, balance=0.0, file_path="bank/data.json"):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        self.file_path = file_path
        self.load_account()

    def load_account(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.balance = data.get("balance", 0.0)
                self.transactions = data.get("transactions", [])
        except FileNotFoundError:
            self.save_account()  # create file if it doesn't exist

    def save_account(self):
        with open(self.file_path, 'w') as file:
            json.dump({
                "balance": self.balance,
                "transactions": self.transactions
            }, file, indent=4)

    @audit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            self.save_account()
        else:
            print("⚠️ Invalid deposit amount.")

    @audit
    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("⚠️ Invalid withdrawal amount.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            self.save_account()

    @audit
    def transfer(self, to_account, amount):
        if amount > self.balance:
            print("❌ Transfer failed: insufficient balance.")
        elif amount <= 0:
            print("⚠️ Invalid transfer amount.")
        else:
            self.withdraw(amount)
            to_account.deposit(amount)
            self.transactions.append(f"Transferred ₹{amount} to {to_account.owner}")
            self.save_account()

    def apply_interest(self, rate=0.02):
        if self.balance > 1000:
            interest = self.balance * rate
            self.balance += interest
            self.transactions.append(f"Interest applied: ₹{round(interest, 2)}")
            self.save_account()

    def show_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

    def show_transactions(self):
        print("\n📜 Transaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for txn in self.transactions:
                print("-", txn)

    def transaction_generator(self, keyword):
        for txn in self.transactions:
            if keyword.lower() in txn.lower():
                yield txn
