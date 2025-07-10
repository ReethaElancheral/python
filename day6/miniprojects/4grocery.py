# 🧩 4. Grocery List Manager

# Topics Covered: **kwargs, list, return, local/global
# Requirements:
# Use **kwargs to add items (item=quantity)
# Create a function to calculate total items
# Return all items sorted alphabetically
# Use global for the inventory list

inventory = []

def add_items(**kwargs):
    global inventory
    for item, qty in kwargs.items():
        inventory.append((item, qty))
    print("✅ Items added to inventory.")

def calculate_total_items():
    return sum(qty for _, qty in inventory)

def get_sorted_inventory():
    return sorted(inventory, key=lambda x: x[0])


add_items(milk=2, rice=5, eggs=12)
add_items(bread=1, apple=6)

total = calculate_total_items()
print(f"\n📦 Total Quantity of Items: {total}")

print("\n📋 Sorted Inventory:")
for item, qty in get_sorted_inventory():
    print(f"{item.capitalize()}: {qty}")
