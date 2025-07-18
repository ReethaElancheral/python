# grocery/checkout.py

import json
import random
from datetime import datetime
from grocery.cart import load_cart

def generate_bill(cart):
    bill_id = random.randint(1000, 9999)
    bill_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill = {
        "bill_id": bill_id,
        "bill_time": bill_time,
        "items": cart["items"],
        "total": cart["total"]
    }
    with open(f'grocery/bill_{bill_id}.json', 'w') as file:
        json.dump(bill, file, indent=4)
    return f"Bill generated with ID: {bill_id}"

def checkout(cart):
    if cart["total"] > 0:
        bill_message = generate_bill(cart)
        cart["items"] = {}
        cart["total"] = 0.0
        return bill_message
    else:
        return "Your cart is empty. Add items before checkout."
