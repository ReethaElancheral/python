# ✅ 9. Simple Shopping Cart

# Objective: Add items and calculate total.
# Requirements:
# Use a dictionary for products and price.
# User selects 3 items (input).
# Store in list and use loop to calculate total.
# Print total bill.

products = {
    "milk": 40,
    "bread": 30,
    "eggs": 60,
    "rice": 100,
    "oil": 150
}

selected_items = []
print("Available products:", ", ".join(products.keys()))
for i in range(1, 4):
    item = input(f"Enter item {i}: ").lower().strip()
    selected_items.append(item)

total = 0
print("\n🧾 **Shopping Summary:**")
for item in selected_items:
    if item in products:
        price = products[item]
        total += price
        print(f"- {item.capitalize():<10}: ₹{price}")
    else:
        print(f"- {item.capitalize():<10}: ❌ Not available")

print(f"\n💰 **Total Bill:** ₹{total}")
