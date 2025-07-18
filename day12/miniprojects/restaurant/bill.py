# restaurant/bill.py
from .offers import apply_discount

TAX_RATE = 0.07  # 7%

def calculate_bill(order):
    subtotal = sum(price for _,_,price in order['items'])
    discount = apply_discount(subtotal)
    taxable = subtotal - discount
    tax = round(taxable * TAX_RATE, 2)
    total = round(taxable + tax, 2)
    return {
        'subtotal': subtotal,
        'discount': discount,
        'tax': tax,
        'total': total
    }

def format_bill(order, bill):
    lines = []
    lines.append(f"Order ID: {order['order_id']}")
    lines.append("Items:")
    for _, name, price in order['items']:
        lines.append(f"  - {name}: ${price:.2f}")
    lines.append(f"Subtotal: ${bill['subtotal']:.2f}")
    lines.append(f"Discount: -${bill['discount']:.2f}")
    lines.append(f"Tax (@{TAX_RATE*100:.0f}%): +${bill['tax']:.2f}")
    lines.append(f"Total Due: ${bill['total']:.2f}")
    return "\n".join(lines)
