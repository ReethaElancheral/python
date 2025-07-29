from functools import wraps
from datetime import datetime

def audit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 Auditing: {func.__name__} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        result = func(*args, **kwargs)
        return result
    return wrapper
