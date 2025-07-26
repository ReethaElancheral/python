# 7. Secure API Token Validator 
# Objective: Validate an API token passed to the function. 
# Requirements: 
#  Check for a valid token using a decorator 
#  Use @validate_token("secret_token") 

#  Deny execution if token is missing/invalid

from functools import wraps

def validate_token(expected_token):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.get("token")
            if token != expected_token:
                print("Invalid or missing token.")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_token("secret_token")
def secure_data_access(**kwargs):
    print("Access granted to secure data")

secure_data_access(token="secret_token")
secure_data_access(token="wrong")
