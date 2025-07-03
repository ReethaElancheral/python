# 20. E-commerce Mini Checkout System

# Objective: Simulate a basic cart checkout.
# Requirements:
# Input: product price, quantity, discount code.
# Validate discount code using in operator.
# Apply discount.
# Calculate total using arithmetic and assignment operators.


valid_discounts = {
    "SAVE10": 10,
    "SALE20": 20,
    "FEST30": 30
}

price = float(input("Enter product price: ₹"))
quantity = int(input("Enter quantity: "))
discount_code = input("Enter discount code (if any): ").upper()

total = price * quantity

if discount_code in valid_discounts:
    discount_percent = valid_discounts[discount_code]
    discount_amount = total * discount_percent / 100
    total -= discount_amount  
    print(f"Discount '{discount_code}' applied: ₹{discount_amount:.2f}")
else:
    print("No valid discount applied.")

print(f"Total amount to pay: ₹{total:.2f}")
