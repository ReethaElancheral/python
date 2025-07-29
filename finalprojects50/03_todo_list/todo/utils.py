# todo/utils.py

import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMEIT] {func.__name__} took {(end - start):.6f} seconds.")
        return result
    return wrapper
