# ✅ 3. Mini Billing System

# Objective: Calculate total bill with conditions.
# Requirements:
# Use dictionary: item → price.
# Use list to take user’s selected items.
# Use for loop to calculate total.
# If total > 1000 → apply 10% discount.
# Use variables, list, dict, float.


items = {
    "milk": 40.0,
    "bread": 30.0,
    "rice": 60.0,
    "eggs": 90.0,
    "oil": 150.0,
    "sugar": 45.0,
    "soap": 25.0
}

selected_items = input("Enter the items you want to buy (comma-separated): ").lower().split(',')

selected_items = [item.strip() for item in selected_items]

total = 0.0

print("\n🧾 Billing Details:")
for item in selected_items:
    if item in items:
        price = items[item]
        total += price
        print(f"{item.capitalize():<10} - ₹{price}")
    else:
        print(f"{item.capitalize():<10} - Not available")

if total > 1000:
    discount = total * 0.10
    total -= discount
    print(f"\n🎁 10% discount applied: -₹{discount:.2f}")


print(f"\nTotal Bill: ₹{total:.2f}")
