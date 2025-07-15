# 9. Restaurant Menu Display System

# Goal: Store menu items and prices.
# Requirements:
# Menu item as tuple: (item_id, item_name, price)
# Store multiple tuples in a list.
# Use for loop to display formatted menu.
# Find expensive item using max() and a lambda.
# Enforce immutability to prevent price tampering.


menu = [
    (1, "Spaghetti Carbonara", 12.99),
    (2, "Margherita Pizza", 9.99),
    (3, "Caesar Salad", 7.49),
    (4, "Grilled Salmon", 18.99),
    (5, "Tiramisu", 5.99)
]


def display_menu(menu):
    print("\n🍴 Restaurant Menu")
    print("----------------------------")
    for item_id, item_name, price in menu:
        print(f"{item_id}. {item_name} - ${price:.2f}")
    print("----------------------------")


def find_expensive_item(menu):
    most_expensive = max(menu, key=lambda item: item[2]) 
    item_id, item_name, price = most_expensive
    print(f"\n💎 Most Expensive Item:")
    print(f"{item_name} - ${price:.2f}")


display_menu(menu)


find_expensive_item(menu)
