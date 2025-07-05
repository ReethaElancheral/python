# ✅ 5. ATM Simulation

# Objective: Basic ATM system with balance check.
# Requirements:
# Set initial balance as a variable.
# Allow 3 operations in a for loop: deposit, withdraw, check balance.
# Use condition to check if withdrawal is valid.

balance = 1000.0

print("🏧 Welcome to ANTILLIA AMBANI ATM")
print("You can perform 3 operations: deposit, withdraw, check")

for i in range(3):
    print(f"\nOperation {i+1}")
    action = input("Enter operation (deposit/withdraw/check): ").lower()

    if action == "deposit":
        amount = float(input("Enter deposit amount: ₹"))
        balance += amount
        print(f"✅ ₹{amount} deposited successfully. Your Balance is: ₹{balance:.2f}")

    elif action == "withdraw":
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount <= balance:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
        else:
            print("❌ Insufficient balance.")

    elif action == "check":
        print(f"💰 Current Balance: ₹{balance:.2f}")

    else:
        print("⚠️ Invalid operation.")

print(f"\n📄 Final Balance: ₹{balance:.2f}")
