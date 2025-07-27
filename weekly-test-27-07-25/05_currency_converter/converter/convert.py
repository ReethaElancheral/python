from .api import get_exchange_rate

def convert_currency(amount, base, target):
    rate = get_exchange_rate(base, target)
    if rate is None:
        raise ValueError("Failed to get exchange rate")
    return amount * rate
