# 7. E-commerce Order Tracker

# Goal: Manage orders in an e-commerce system.
# Requirements:
# Store orders as (order_id, customer_name, (item1, item2, item3))
# Use tuple nesting to represent items in each order.
# Iterate through orders to generate a report.
# Display all items using nested loop and unpacking.
# Prevent accidental changes in the order items.


orders = [
    (1001, "Alice", ("Laptop", "Mouse", "Keyboard")),
    (1002, "Bob", ("Smartphone", "Charger")),
    (1003, "Charlie", ("Tablet", "Stylus", "Screen Protector")),
    (1004, "David", ("Smartwatch", "Band")),
    (1005, "Elaine", ("Headphones", "Case"))
]

def generate_order_report(order_list):
    print("\n📦 Order Report")
    print("------------------------------")
    for order_id, customer, items in order_list:
        print(f"Order #{order_id} | Customer: {customer}")
        print("Items:")
        for item in items:
            print(f"  - {item}")
        print("------------------------------")

def count_item_occurrences(order_list, item_name):
    return sum(item_name in items for _, _, items in order_list)


generate_order_report(orders)

item_to_search = "Charger"
occurrences = count_item_occurrences(orders, item_to_search)
print(f"\n📊 '{item_to_search}' appears in {occurrences} order(s).")
