# 12. Notification System with Customizable Headers 
# Objective: Add custom notification headers and footers. 
# Requirements: 
#  Use decorator with arguments for header/footer text 
#  Wrap function output with given values 
#  Preserve return values using functools.wraps

from functools import wraps

def notification(header, footer):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"=== {header} ===")
            result = func(*args, **kwargs)
            print(f"=== {footer} ===")
            return result
        return wrapper
    return decorator

@notification("Start Notification", "End Notification")
def notify_user(message):
    print(f"Message: {message}")

# Example:
notify_user("Your order has been placed.")
