# 18. Online Order History

# Description: Track user orders in a list.
# Add new orders.
# Remove canceled orders.
# Show last 5 orders.
# Display order count.



orders = []

def show_orders():
    if not orders:
        print("No orders placed yet.")
    else:
        print("\n📦 All Orders:")
        for i, order in enumerate(orders, 1):
            print(f"{i}. {order}")

def add_order():
    order = input("Enter new order: ").strip()
    if order:
        orders.append(order)
        print(f"Order '{order}' added.")
    else:
        print("Order cannot be empty.")

def remove_order():
    if not orders:
        print("No orders to remove.")
        return
    order = input("Enter order to cancel/remove: ").strip()
    if order in orders:
        orders.remove(order)
        print(f"Order '{order}' removed.")
    else:
        print(f"Order '{order}' not found.")

def show_last_five():
    print("\n📋 Last 5 Orders:")
    for order in orders[-5:]:
        print(order)

def show_order_count():
    print(f"\nTotal orders placed: {len(orders)}")


while True:
    print("\n--- Online Order History ---")
    print("1. Show All Orders")
    print("2. Add Order")
    print("3. Remove Order")
    print("4. Show Last 5 Orders")
    print("5. Show Order Count")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_orders()
    elif choice == "2":
        add_order()
    elif choice == "3":
        remove_order()
    elif choice == "4":
        show_last_five()
    elif choice == "5":
        show_order_count()
    elif choice == "6":
        print("Exiting Order History. Bye!")
        break
    else:
        print("Invalid choice.")
