from cart.discounts import apply_discount

def add_to_cart(cart, products, product_id, quantity):
    if product_id in products and products[product_id][2] >= quantity:
        cart.append((product_id, quantity))
        print(f"Added {quantity} of {products[product_id][0]} to cart.")
    else:
        print("Product not available or insufficient stock.")

def remove_from_cart(cart, product_id, quantity):
    for i, (pid, qty) in enumerate(cart):
        if pid == product_id:
            if qty > quantity:
                cart[i] = (pid, qty - quantity)
            else:
                cart.pop(i)
            print(f"Removed {quantity} of {product_id} from cart.")
            return
    print("Item not found in cart.")

def checkout(cart, products):
    print("\n--- BILL ---")
    total = 0
    unique_items = set()
    for product_id, qty in cart:
        name, price, _ = products[product_id]
        amount = price * qty
        total += amount
        unique_items.add(product_id)
        print(f"{name:<15} x {qty:<3} = ₹{amount:.2f}")
    
    total = apply_discount(total)
    print(f"Total (after discount): ₹{total:.2f}")
    print(f"Unique items bought: {len(unique_items)}")
