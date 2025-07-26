# 14. Throttle Controller 
# Objective: Limit how many times a function can run in a minute. 
# Requirements: 
#  Use decorator with parameters (e.g., @throttle(10)) 
#  If called more than 10 times in a minute, raise error 
#  Log blocked calls 

import time
from functools import wraps
from collections import defaultdict

def throttle(max_calls_per_minute):
    call_times = defaultdict(list)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            key = func.__name__
            # Remove old timestamps (older than 60 seconds)
            call_times[key] = [t for t in call_times[key] if now - t < 60]

            if len(call_times[key]) >= max_calls_per_minute:
                print("⛔ Throttled: Too many calls.")
                return
            call_times[key].append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@throttle(3)
def fetch_data():
    print("✅ Fetching data from server...")

# Example:
for _ in range(5):
    fetch_data()
    time.sleep(1)
