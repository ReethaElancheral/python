# converter/utils.py
from functools import wraps
import time

_cached_data = {}

def cache_rates(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "rates" in _cached_data:
            return _cached_data["rates"]
        result = func(*args, **kwargs)
        _cached_data["rates"] = result
        return result
    return wrapper
