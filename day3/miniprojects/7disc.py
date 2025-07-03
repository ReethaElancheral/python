# 7. Product Discount System

# Objective: Calculate final price after discount.
# Requirements:
# Input: product name, price, discount %.
# Use arithmetic for discount.
# Use assignment operators.
# Use f-string to display output.


product = input("Enter product name: ")
price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount percentage: "))


discount_amount = price * discount_percent / 100
price -= discount_amount  

print(f"\nProduct: {product}")
print(f"Discount: ₹{discount_amount:.2f}")
print(f"Final Price after discount: ₹{price:.2f}")
