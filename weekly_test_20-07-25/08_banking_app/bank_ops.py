from datetime import datetime

def deposit(user, amount):
    if amount <= 0:
        print("Invalid deposit amount.")
        return
    user["balance"] += amount
    user["transactions"].append((datetime.now().strftime("%Y-%m-%d %H:%M"), "DEPOSIT", amount))
    print(f"₹{amount} deposited.")

def withdraw(user, amount, min_balance=100):
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return
    if user["balance"] - amount < min_balance:
        print("Insufficient balance. Maintain minimum ₹100.")
        return
    user["balance"] -= amount
    user["transactions"].append((datetime.now().strftime("%Y-%m-%d %H:%M"), "WITHDRAW", amount))
    print(f"₹{amount} withdrawn.")

def view_statement(user):
    print("\n--- Transaction History ---")
    for date, txn_type, amount in user["transactions"]:
        print(f"{date} | {txn_type} | ₹{amount}")
    print(f"\nCurrent Balance: ₹{user['balance']}")

def get_unique_transaction_types(user):
    return set(txn_type for _, txn_type, _ in user["transactions"])
