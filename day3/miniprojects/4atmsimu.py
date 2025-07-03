# 4. Simple ATM Simulation

# Objective: Simulate basic ATM operations.
# Requirements:
# Input: initial balance, deposit or withdrawal.
# Use if to check sufficient balance.
# Use +=, -= for assignment.
# Use comparison operators.
# Use f-string to show balance and transaction result.


balance = float(input("Enter your initial balance: "))

action = input("Do you want to deposit or withdraw? ").lower()

if action == "deposit":
    amount = float(input("Enter amount to deposit: "))
    balance += amount  
    print(f"₹{amount} deposited successfully.")
    print(f"Updated balance: ₹{balance:.2f}")

elif action == "withdraw":
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance: 
        balance -= amount  
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining balance: ₹{balance:.2f}")
    else:
        print(f"Insufficient balance! Your current balance is ₹{balance:.2f}")

else:
    print("Invalid action. Please enter 'deposit' or 'withdraw'.")
