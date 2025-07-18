def add_to_cart(cart, item_id, name, category, price):
    key = (item_id,)  # Tuple for immutability
    if key in cart:
        print(f"Item '{name}' is already in the cart.")
        return

    cart[key] = {
        "name": name,
        "category": category,
        "price": price
    }
    print(f"Added '{name}' to cart.")

def view_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    print("\n--- Shopping Cart ---")
    total = 0
    for item_id, info in cart.items():
        print(f"ID: {item_id[0]} | {info['name']} | ₹{info['price']} | Category: {info['category']}")
        total += info["price"]
    print(f"Total: ₹{total:.2f}")

def get_unique_categories(cart):
    categories = {item["category"] for item in cart.values()}
    return categories
