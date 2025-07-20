def add_item(inventory, categories, suppliers):
    item = input("Item name: ").strip()
    quantity = int(input("Quantity: "))
    price = float(input("Price (INR): "))
    category = input("Category: ").strip()
    supplier = input("Supplier name: ").strip()

    inventory[item] = ((quantity, price), category, supplier)
    categories.add(category)
    suppliers.add(supplier)
    print(f"{item} added successfully.")

def remove_item(inventory):
    item = input("Enter item to remove: ").strip()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed.")
    else:
        print("Item not found.")

def update_stock(inventory):
    item = input("Enter item to update: ").strip()
    if item in inventory:
        quantity = int(input("New quantity: "))
        price = float(input("New price (INR): "))
        old_category = inventory[item][1]
        old_supplier = inventory[item][2]
        inventory[item] = ((quantity, price), old_category, old_supplier)
        print(f"{item} updated.")
    else:
        print("Item not found.")

def list_by_category(inventory):
    category = input("Enter category to list: ").strip()
    found = False
    for item, ((qty, price), cat, _) in inventory.items():
        if cat == category:
            print(f"{item}: Qty={qty}, Price=₹{price}")
            found = True
    if not found:
        print("No items found in this category.")

def view_inventory(inventory, suppliers):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- Inventory ---")
    for item, ((qty, price), category, supplier) in inventory.items():
        print(f"{item}: Qty={qty}, Price=₹{price}, Category={category}, Supplier={supplier}")
    print("\nUnique suppliers:", ", ".join(suppliers))
