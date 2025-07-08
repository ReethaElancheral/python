# ✅ 6. ATM Withdrawal Limit System

# Objective: Simulate withdrawal up to ₹10,000 per day.
# Requirements:
# Use while loop to allow multiple transactions.
# Stop when total withdrawal reaches 10,000 or user types “stop”.
# Use break to exit early on error or stop request.

daily_limit = 10000
withdrawn = 0

while withdrawn < daily_limit:
    user_input = input("Enter amount to withdraw or type 'stop' to exit: ")
    
    if user_input.lower() == "stop":
        print("Transaction stopped by user.")
        break

    if not user_input.isdigit():
        print("Invalid amount! Please enter a valid number.")
        break

    amount = int(user_input)

    if withdrawn + amount > daily_limit:
        print("Limit exceeded! You can only withdraw up to ₹", daily_limit - withdrawn)
        break

    withdrawn += amount
    print(f"₹{amount} withdrawn. Total withdrawn: ₹{withdrawn}")

else:
    print("₹10,000 daily limit reached.")
