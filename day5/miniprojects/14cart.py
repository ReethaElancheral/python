# ✅ 14. Shopping Cart Input App

# Objective: Enter product names into cart.
# Requirements:
# Use infinite while True loop.
# User types product name or “done” to stop.
# Use continue to skip empty input.
# Print product list in else.

cart = []

while True:
    product = input("Enter product name (or 'done' to finish): ").strip()
    if product == "done":
        break
    if product == "":
        print("Empty input, try again.")
        continue
    cart.append(product)
else:
    pass

print("Products in your cart:")
for item in cart:
    print(f"- {item}")
