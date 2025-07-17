# shopping_cart/checkout.py

from .cart import total

def process_checkout(cart):
    tot = total(cart)
    print(f"Total amount: ${tot:.2f}")
    return tot
