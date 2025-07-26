# 10. Function Call Counter 
# Objective: Count how many times a function has been called. 
# Requirements: 
#  Create a decorator that tracks call count 
#  Print or log total calls every time it runs 
#  Allow reset of count via an attribute


from functools import wraps
def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    wrapper.reset = lambda: setattr(wrapper, 'count', 0)
    return wrapper

@call_counter
def greet():
    print("Hello!")

greet()
greet()
greet()
greet.reset()
greet()
