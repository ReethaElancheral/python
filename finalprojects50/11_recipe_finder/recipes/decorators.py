import functools
import datetime

def log_search(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        ingredient = args[0] if args else None
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Searching recipes with ingredient: {ingredient}")
        return func(self, *args, **kwargs)
    return wrapper
