# 12. Bank Account Simulation

# Description: Simulate basic banking operations.
# Requirements:
# - Structure: {account_number: {"name": ..., "balance": ...}}
# - Deposit, withdraw operations
# - Use get() to avoid account not found error
# - Flag low-balance accounts (<1000) using comprehension


accounts = {
    1001: {"name": "Alice", "balance": 1500},
    1002: {"name": "Bob", "balance": 500},
    1003: {"name": "Charlie", "balance": 2000},
}

def deposit(account_number, amount):
    """Deposit money into an account."""
    account = accounts.get(account_number)
    if account:
        account["balance"] += amount
        print(f"Deposited ₹{amount} to account {account_number}. New balance: ₹{account['balance']}")
    else:
        print(f"Account {account_number} not found.")

def withdraw(account_number, amount):
    """Withdraw money from an account."""
    account = accounts.get(account_number)
    if account:
        if account["balance"] >= amount:
            account["balance"] -= amount
            print(f"Withdrew ₹{amount} from account {account_number}. New balance: ₹{account['balance']}")
        else:
            print(f"Insufficient balance in account {account_number}.")
    else:
        print(f"Account {account_number} not found.")

def low_balance_alert():
    """Flag accounts with balance below ₹1000."""
    return {acc_num: details for acc_num, details in accounts.items() if details["balance"] < 1000}

def display_account(account_number):
    """Display account details."""
    account = accounts.get(account_number)
    if account:
        print(f"Account {account_number}: {account['name']}, Balance: ₹{account['balance']}")
    else:
        print(f"Account {account_number} not found.")


deposit(1001, 500)


withdraw(1002, 200)


display_account(1003)


print("Low balance accounts:", low_balance_alert())
