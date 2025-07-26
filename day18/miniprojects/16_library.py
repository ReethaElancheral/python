# 16. Decorated Math Library 
# Objective: Add decorators to math functions. 
# Requirements: 
#  @validate_numeric_input 
#  @log_output 
#  @timeit 
#  Functions: add(), multiply(), divide() 

import time
from functools import wraps

def validate_numeric_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(i, (int, float)) for i in args):
            raise TypeError("All inputs must be numeric.")
        return func(*args, **kwargs)
    return wrapper

def log_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned: {result}")
        return result
    return wrapper

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timeit
@log_output
@validate_numeric_input
def add(a, b):
    return a + b

@timeit
@log_output
@validate_numeric_input
def multiply(a, b):
    return a * b

@timeit
@log_output
@validate_numeric_input
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Example usage:
add(10, 5)
multiply(4, 6)
divide(10, 2)
