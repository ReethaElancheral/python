# 13. Inventory Management System

# Concepts: Class, Encapsulation, Dunder Methods
# Classes:  Item, Inventory,  Supplier
# Requirements:
# Add, update, remove items
# Use __contains__, __getitem__
# Secure supplier info with encapsulation

class Supplier:
    def __init__(self, name, contact):
        self.__name = name           # private
        self.__contact = contact     # private

    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    def __str__(self):
        return f"Supplier: {self.__name}, Contact: {self.__contact}"

class Item:
    def __init__(self, item_id, name, quantity, supplier):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.supplier = supplier    

    def __str__(self):
        return (f"Item ID: {self.item_id}, Name: {self.name}, "
                f"Quantity: {self.quantity}, Supplier: {self.supplier.get_name()}")

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item
        print(f"Added item: {item.name}")

    def update_quantity(self, item_id, quantity):
        if item_id in self.items:
            self.items[item_id].quantity = quantity
            print(f"Updated quantity of item ID {item_id} to {quantity}")
        else:
            print(f"Item ID {item_id} not found.")

    def remove_item(self, item_id):
        if item_id in self.items:
            removed = self.items.pop(item_id)
            print(f"Removed item: {removed.name}")
        else:
            print(f"Item ID {item_id} not found.")

    def __contains__(self, item_id):
        return item_id in self.items

    def __getitem__(self, item_id):
        return self.items.get(item_id, None)

    def display_inventory(self):
        print("Inventory:")
        for item in self.items.values():
            print(item)

def main():
    # Create suppliers
    supplier1 = Supplier("ABC Traders", "9876543210")
    supplier2 = Supplier("XYZ Suppliers", "9123456780")

    # Create inventory
    inventory = Inventory()

    # Add items
    item1 = Item(101, "Laptop", 10, supplier1)
    item2 = Item(102, "Mouse", 50, supplier2)
    item3 = Item(103, "Keyboard", 30, supplier1)

    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)

    # Display inventory
    inventory.display_inventory()

    # Update quantity
    inventory.update_quantity(102, 60)

    # Check if item exists
    print(102 in inventory)  # True
    print(999 in inventory)  # False

    # Access item by item_id
    item = inventory[101]
    if item:
        print(f"Accessed item: {item}")

    # Remove an item
    inventory.remove_item(103)

    # Final inventory
    inventory.display_inventory()

if __name__ == "__main__":
    main()
