# 19. Class Method Logger (Class Decorator) 
# Objective: Log all method calls inside a class using class-level decorator. 
# Requirements: 
#  Decorate class with @log_methods 
#  Automatically wrap all methods with logger 
#  Print method name and arguments 

from functools import wraps

def log_methods(cls):
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and not attr_name.startswith("__"):
            @wraps(attr)
            def wrapper(self, *args, __method=attr, **kwargs):
                print(f"[LOG] Calling {__method.__name__} with args: {args}, kwargs: {kwargs}")
                return __method(self, *args, **kwargs)
            setattr(cls, attr_name, wrapper)
    return cls

@log_methods
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# Example usage:
calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 3))
