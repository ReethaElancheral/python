# 6. Smart Logger with File Writing 
# Objective: Automatically log outputs to a file for every function call. 
# Requirements: 
#  Create a decorator that writes logs to log.txt 
#  Include timestamp, function name, and result 
#  Use a parameter to control log level 


from datetime import datetime
from functools import wraps


def file_logger(level="INFO"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open("log.txt", "a") as f:
                f.write(f"[{datetime.now()}] [{level}] {func.__name__} returned {result}\n")
            return result
        return wrapper
    return decorator

@file_logger("DEBUG")
def calculate_sum(a, b):
    return a + b

calculate_sum(2, 3)
