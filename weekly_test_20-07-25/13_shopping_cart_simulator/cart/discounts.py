def apply_discount(total_amount):
    if total_amount > 10000:
        print("Discount applied: ₹500")
        return total_amount - 500
    return total_amount
