# 19. Mobile Recharge Validator

# Objective: Validate mobile number and recharge.
# Requirements:
# Input: mobile number, recharge amount.
# Check:
# Mobile number has 10 digits.
# Amount > 10.
# Use len(), logical and comparison operators.

mobile_number = input("Enter your 10-digit mobile number: ")
recharge_amount = float(input("Enter recharge amount: ₹"))

if len(mobile_number) == 10 and mobile_number.isdigit():
    if recharge_amount > 10:
        print(f"Recharge of ₹{recharge_amount} successful for mobile {mobile_number}.")
    else:
        print("Recharge amount must be greater than ₹10.")
else:
    print("Invalid mobile number. Please enter a 10-digit numeric mobile number.")
