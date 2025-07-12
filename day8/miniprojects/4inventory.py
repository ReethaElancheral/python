# 4. Inventory System for a Shop

# Description: Manage a shop’s item inventory.
# Use list of products.
# Add, update quantity, and delete products.
# Use in to check if a product exists.
# Display all items using loops.


inventory = [
    ["apple", 10],
    ["banana", 20],
    ["chocolate", 15]
]

def show_inventory():
    if not inventory:
        print("📦 Inventory is empty.")
    else:
        print("\n📋 Current Inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item[0]} - Quantity: {item[1]}")

def add_product():
    name = input("Enter product name to add: ").lower()
    for item in inventory:
        if item[0] == name:
            print(f"{name} already exists. Use 'Update' to change quantity.")
            return
    qty = int(input(f"Enter quantity for {name}: "))
    inventory.append([name, qty])
    print(f"{name} added with quantity {qty}.")

def update_quantity():
    name = input("Enter product name to update: ").lower()
    for item in inventory:
        if item[0] == name:
            qty = int(input(f"Enter new quantity for {name}: "))
            item[1] = qty
            print(f"{name} quantity updated to {qty}.")
            return
    print(f"{name} not found in inventory.")

def delete_product():
    name = input("Enter product name to delete: ").lower()
    for item in inventory:
        if item[0] == name:
            inventory.remove(item)
            print(f"{name} removed from inventory.")
            return
    print(f"{name} not found in inventory.")

def check_product():
    name = input("Enter product name to check: ").lower()
    if any(item[0] == name for item in inventory):
        print(f"{name} is available in the inventory.")
    else:
        print(f"{name} is NOT in the inventory.")


while True:
    print("\n--- Shop Inventory Menu ---")
    print("1. Show Inventory")
    print("2. Add Product")
    print("3. Update Quantity")
    print("4. Delete Product")
    print("5. Check Product Exists")
    print("6. Exit")

    choice = input("Choose an option (1–6): ")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_quantity()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        check_product()
    elif choice == "6":
        print("Goodbye! 👋 Inventory closed.")
        break
    else:
        print("Invalid option. Choose between 1–6.")
