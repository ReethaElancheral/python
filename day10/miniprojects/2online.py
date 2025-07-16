# 2. Online Shopping Cart

# Description: Simulate a shopping cart for an online store.
# Requirements:
# - Cart format: {item_name: {"quantity": x, "price": y}}
# - Add, update, or remove items
# - Calculate total bill
# - Remove out-of-stock items using pop()
# - Show highest value item
# - Apply .values() and .items() for bill summary
# - Use nested dictionaries and in keyword


cart = {}

def add_item(item, qty, price):
    """Add a new item or update existing one."""
    if item in cart:
        cart[item]["quantity"] += qty
        cart[item]["price"] = price  
    else:
        cart[item] = {"quantity": qty, "price": price}

def remove_item(item):
    """Remove an item completely (e.g., out-of-stock)."""
    return cart.pop(item, None)

def update_quantity(item, qty):
    """Update quantity for existing item."""
    if item in cart:
        if qty > 0:
            cart[item]["quantity"] = qty
        else:
            remove_item(item)

def calculate_total():
    """Calculate total bill: sum(qty * price)."""
    return sum(v["quantity"] * v["price"] for v in cart.values())

def highest_value_item():
    """Return the item contributing highest to the bill."""
    return max(cart.items(), key=lambda kv: kv[1]["quantity"] * kv[1]["price"], default=None)


add_item("apple", 3, 0.5)
add_item("banana", 5, 0.3)
add_item("apple", 2, 0.55)  


remove_item("banana")


for name, info in cart.items():
    print(f"{name.title()}: {info['quantity']} × ₹{info['price']:.2f} = ₹{info['quantity'] * info['price']:.2f}")

print("Total Bill: ₹", calculate_total())


hv = highest_value_item()
if hv:
    item_name, info = hv
    total_value = info["quantity"] * info["price"]
    print(f"Highest value item: {item_name} – ₹{total_value:.2f}")
