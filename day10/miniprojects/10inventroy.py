# 10. Inventory Management System

# Description: Track store inventory levels.
# Requirements:
# - {item_name: {"stock": ..., "min_required": ..., "supplier": ...}}
# - Alert items below minimum
# - Add new items using setdefault()
# - Delete discontinued items
# - Export low-stock items using dictionary comprehension



inventory = {
    "Laptop": {"stock": 10, "min_required": 5, "supplier": "TechCorp"},
    "Smartphone": {"stock": 2, "min_required": 5, "supplier": "MobileInc"},
    "Headphones": {"stock": 15, "min_required": 10, "supplier": "AudioLtd"},
    "Keyboard": {"stock": 3, "min_required": 5, "supplier": "KeyTech"}
}

def alert_low_stock():
    """Alert items with stock below minimum required."""
    return {item: details for item, details in inventory.items() if details["stock"] < details["min_required"]}

def add_item(item_name, stock, min_required, supplier):
    """Add a new item or update existing item."""
    inventory.setdefault(item_name, {"stock": 0, "min_required": 0, "supplier": ""})
    inventory[item_name]["stock"] += stock
    inventory[item_name]["min_required"] = min_required
    inventory[item_name]["supplier"] = supplier

def delete_item(item_name):
    """Delete an item from inventory."""
    inventory.pop(item_name, None)

def export_low_stock_items():
    """Export items with stock below minimum required."""
    return {item: details for item, details in inventory.items() if details["stock"] < details["min_required"]}


print("Low stock alerts:", alert_low_stock())
add_item("Smartwatch", 5, 3, "GadgetCo")
print("Updated inventory:", inventory)
delete_item("Keyboard")
print("Inventory after deletion:", inventory)
print("Low stock items:", export_low_stock_items())
