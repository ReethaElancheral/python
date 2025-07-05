# ✅ 19. Simple Discount Engine

# Objective: Apply discount based on price.
# Requirements:
# Input: product price.
# Use if-elif-else:
# 2000: 20% off, >1000: 10%, else: No discount

price = float(input("Enter product price: ₹"))

if price >= 2000:
    discount = price * 0.20
elif price > 1000:
    discount = price * 0.10
else:
    discount = 0

final_price = price - discount

print(f"Original Price: ₹{price:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Price after discount: ₹{final_price:.2f}")
