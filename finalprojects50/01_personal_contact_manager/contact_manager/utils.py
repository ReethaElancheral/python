# contact_manager/utils.py

from functools import wraps

def log_actions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
