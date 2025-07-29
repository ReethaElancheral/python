# weatherapp/utils.py

import time
from functools import wraps

def retry(max_retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"API call failed: {e}. Retrying ({attempts}/{max_retries})...")
                    time.sleep(delay)
            print("Max retries reached. Operation failed.")
            return None
        return wrapper
    return decorator
