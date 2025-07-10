# 🧩 5. ATM Simulator

# Topics Covered: nested functions, pass, return, conditions
# Requirements:
# Validate PIN using a function
# Nested functions for deposit, withdrawal
# Use pass in change_pin() function placeholder
# Print final balance

def atm_simulator():
    correct_pin = "1234"
    balance = 5000

    def validate_pin(pin):
        return pin == correct_pin

    def deposit(amount):
        nonlocal balance
        balance += amount
        print(f"💰 Deposited ₹{amount}. New balance: ₹{balance}")

    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            print(f"💸 Withdrew ₹{amount}. Remaining balance: ₹{balance}")
        else:
            print("❌ Insufficient balance!")

    def change_pin():
        pass

   
    entered_pin = input("🔐 Enter your PIN: ")
    if validate_pin(entered_pin):
        print("✅ Access granted!")

        while True:
            print("\n🏧 ATM Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")

            choice = input("Choose an option (1-3): ")

            if choice == "1":
                amt = float(input("Enter deposit amount: ₹"))
                deposit(amt)
            elif choice == "2":
                amt = float(input("Enter withdrawal amount: ₹"))
                withdraw(amt)
            elif choice == "3":
                print(f"👋 Thank you! Final Balance: ₹{balance}")
                break
            else:
                print("⚠️ Invalid choice. Try again.")
    else:
        print("❌ Invalid PIN!")


atm_simulator()
