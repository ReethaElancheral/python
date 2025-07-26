# 5. Input Type Validation System 
# Objective: Ensure a function receives correct argument types. 
# Requirements: 
#  Create a decorator that checks types dynamically 
#  Raise TypeError on mismatch 
#  Use with multiple functions like add(int, int) or concat(str, str) 


from functools import wraps

def validate_types(*expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"{arg} is not {expected}")
            return func(*args)
        return wrapper
    return decorator

@validate_types(int, int)
def add(a, b):
    return a + b

@validate_types(str, str)
def concat(a, b):
    return a + b

print(add(3, 4))
print(concat("Hello", "World"))
