# 3. Auto-Retry Mechanism for Network Functions 
# Objective: Retry a function up to 3 times if an exception occurs. 
# Requirements: 
#  Use a retry decorator with parameters: 
# o max_retries 
# o delay 
#  Log each attempt and final status

import time
from functools import wraps


def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed: {e}")
                    time.sleep(delay)
            print("Max retries reached. Aborting.")
        return wrapper
    return decorator

@retry(max_retries=3, delay=2)
def unstable_network():
    raise ConnectionError("No network")

unstable_network()
