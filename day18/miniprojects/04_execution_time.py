# 4. Execution Time Benchmarking Tool 
# Objective: Measure and report execution time of critical functions. 
# Requirements: 
#  Create a @timeit decorator 
#  Record start & end time 
#  Print execution duration 
#  Use for performance comparison 

import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper

@timeit
def slow_function():
    time.sleep(1.2)
    return "Done"

slow_function()
