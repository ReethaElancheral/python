# grocery/cart.py

import json
import random
from datetime import datetime
from grocery.items import ITEMS

def load_cart():
    try:
        with open('grocery/data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"items": {}, "total": 0.0}

def save_cart(cart):
    with open('grocery/data.json', 'w') as file:
        json.dump(cart, file, indent=4)

def add_item(cart, item_name, quantity):
    if item_name in ITEMS:
        price = ITEMS[item_name]
        total_price = price * quantity
        if item_name in cart["items"]:
            cart["items"][item_name]["quantity"] += quantity
            cart["items"][item_name]["total_price"] += total_price
        else:
            cart["items"][item_name] = {"quantity": quantity, "total_price": total_price}
        cart["total"] += total_price
        save_cart(cart)
        return f"Added {quantity} {item_name}(s) to your cart."
    else:
        return f"Item '{item_name}' is not available."

def remove_item(cart, item_name):
    if item_name in cart["items"]:
        cart["total"] -= cart["items"][item_name]["total_price"]
        del cart["items"][item_name]
        save_cart(cart)
        return f"Removed '{item_name}' from your cart."
    else:
        return f"Item '{item_name}' not found in your cart."
