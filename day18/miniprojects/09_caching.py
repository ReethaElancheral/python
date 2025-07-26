# 9. Caching / Memoization Decorator 
# Objective: Cache function results to avoid recomputation. 
# Requirements: 
#  Use a dictionary to store results 
#  Use input arguments as cache keys 
#  Return cached value if already computed


from functools import wraps
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fib(n):
    if n in (0, 1): return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Efficient with caching
