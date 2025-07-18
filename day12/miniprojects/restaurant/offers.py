# restaurant/offers.py
def apply_discount(subtotal):
    """Apply 10% discount if subtotal ≥ $20"""
    if subtotal >= 20:
        return round(subtotal * 0.10, 2)
    return 0.0
