def add_device(inventory, brands_set, device_type, number, brand, model, price):
    device_id = (device_type.upper(), number)

    if device_id in inventory:
        print(f"Device {device_id} already exists.")
        return

    brands_set.add(brand)
    inventory[device_id] = {
        "brand": brand,
        "model": model,
        "price": price
    }

    print(f"Device {device_id} added successfully.")

def display_inventory(inventory, brands_set):
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n--- Device Inventory ---")
    for device_id, info in inventory.items():
        print(f"ID: {device_id}")
        print(f"  Brand: {info['brand']}")
        print(f"  Model: {info['model']}")
        print(f"  Price: ${info['price']}")
    print(f"\nUnique Brands: {', '.join(brands_set)}")
