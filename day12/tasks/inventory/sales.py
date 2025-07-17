

from .stock import update_stock

def process_sale(item, quantity):
    print(f"Processing sale for {item}, quantity: {quantity}")
    update_stock(item, -quantity)
