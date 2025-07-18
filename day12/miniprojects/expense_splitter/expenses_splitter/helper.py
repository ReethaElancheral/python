from decimal import Decimal, InvalidOperation

def validate_amount(value):
    try:
        amount = Decimal(value)
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return amount
    except (InvalidOperation, ValueError):
        raise ValueError(f"Invalid amount: {value}")
