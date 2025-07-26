# 17. Alert Decorator for Anomalies 
# Objective: Trigger alerts when a function output exceeds a threshold. 
# Requirements: 
#  Decorator takes threshold parameter 
#  Alert (print message) if result > threshold 
#  Works with sensor data simulation 

from functools import wraps

def alert_on_threshold(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f"[ALERT] Value {result} exceeds threshold of {threshold}!")
            return result
        return wrapper
    return decorator

@alert_on_threshold(75)
def get_sensor_data():
    import random
    return random.randint(50, 100)

# Example usage:
get_sensor_data()
