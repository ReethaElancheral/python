# 1. API Request Logger 

# Objective: Log every function that simulates an API call. 
# Requirements: 
#  Use a decorator to log: 
# o Function name 
# o Timestamp 
# o Status (Success/Fail) 
#  Use *args and **kwargs to log parameters 
#  Use functools.wraps to preserve metadata 


from functools import wraps
from datetime import datetime

def api_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            result = func(*args, **kwargs)
            status = "Success"
        except Exception as e:
            result = None
            status = f"Fail ({e})"
        print(f"[{timestamp}] Function: {func.__name__} | Args: {args}, Kwargs: {kwargs} | Status: {status}")
        return result
    return wrapper

@api_logger
def simulate_api_call(endpoint, data):
    if endpoint != "/valid":
        raise ValueError("Invalid endpoint")
    return {"status": "ok", "data": data}

simulate_api_call("/valid", {"id": 1})
simulate_api_call("/invalid", {})
