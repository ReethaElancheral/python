# tracker/utils.py

from functools import wraps

def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
    return wrapper
