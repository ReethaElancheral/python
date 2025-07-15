# 4. Bank Account Manager

# Goal: Manage customer account details using tuples.
# Requirements:
# Store customer data as (account_number, name, (balance, status))
# Use nested tuples for balance and status.
# Access/update display using slicing and indexing.
# Unpack customer data in reports.
# Prevent changes to account data using immutability.

customers = [
    (101, "Nisha",   (1500.0, "active")),
    (102, "Reetha",     ( 250.0, "inactive")),
    (103, "Mannavan",    (3200.5, "active")),
    (104, "Yazh",   ( 780.0, "active"))
]

def show_customers():
    print("\n📋 Customer Accounts")
    print("----------------------------")
    for acct_num, name, info in customers:
        balance, status = info
        print(f"Acct #{acct_num} | {name} | Balance: ₹{balance:.2f} | Status: {status}")
    print("----------------------------")

def find_customer(acct_list, acct_number):
    for idx, record in enumerate(acct_list):
        if record[0] == acct_number:
            return idx
    return None


def update_account():
    acct = int(input("Enter account number to update: "))
    idx = find_customer(customers, acct)
    if idx is not None:
        acct_num, name, (balance, status) = customers[idx]
        print(f"Current → Balance: ₹{balance}, Status: {status}")
        new_bal = input("New balance (enter to skip): ").strip()
        new_st = input("New status (enter to skip): ").strip()
        if new_bal:
            balance = float(new_bal)
        if new_st:
            status = new_st
      
        customers[idx] = (acct_num, name, (balance, status))
        print("✅ Account updated.")
    else:
        print("Account not found.")


while True:
    print("\n--- Bank Account Manager ---")
    print("1. Show all accounts")
    print("2. Update an account")
    print("3. Exit")
    choice = input("Choose (1–3): ")

    if choice == "1":
        show_customers()
    elif choice == "2":
        update_account()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
