# shopping_cart/cart.py

from .items import make_item

def create_cart():
    return []

def add_item(cart, name, price):
    cart.append(make_item(name, price))

def remove_item(cart, name):
    return [item for item in cart if item["name"] != name]

def total(cart):
    return sum(item["price"] for item in cart)
