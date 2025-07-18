# restaurant/order.py
import random
from .menu import MENU

def create_order(selected_items):
    """
    selected_items: list of ints (menu keys)
    Returns: dict with order_id, items (key, name, price)
    """
    order_id = random.randint(1000, 9999)
    items = []
    for key in selected_items:
        if key in MENU:
            name, price = MENU[key]
            items.append((key, name, price))
    return {'order_id': order_id, 'items': items}
