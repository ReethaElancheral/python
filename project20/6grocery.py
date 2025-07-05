# ✅ 6. Grocery Basket Price Calculator

# Objective: Calculate basket total and apply offer.
# Requirements:
# Use dictionary: item → price.
# Input: list of selected items.
# Use for loop to sum prices.
# If user buys more than 5 items → apply ₹50 off.

grocery_prices = {
    "milk": 40,
    "bread": 30,
    "eggs": 60,
    "rice": 100,
    "oil": 150,
    "sugar": 45,
    "salt": 20,
    "soap": 25,
    "butter": 55
}


items_input = input("Enter grocery items (comma-separated): ").lower().split(',')

selected_items = [item.strip() for item in items_input]

total = 0
print("\n🛒 Basket Summary:")
for item in selected_items:
    if item in grocery_prices:
        price = grocery_prices[item]
        total += price
        print(f"{item.capitalize():<10} - ₹{price}")
    else:
        print(f"{item.capitalize():<10} - ❌ Not available")

if len(selected_items) > 5:
    total -= 50
    print("\n🎁 ₹50 Offer Applied (more than 5 items)")
    
print(f"\n🧾 Total Amount: ₹{total}")
