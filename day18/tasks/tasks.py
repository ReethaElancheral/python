# Basic Decorator Tasks 

# 1. Write a basic decorator that prints “Function started” before execution. 

def start_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)
    return wrapper

@start_decorator
def greet():
    print("Hello!")

greet()


# 2. Create a decorator that prints the name of the function being called. 

def name_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@name_decorator
def say_hi():
    print("Hi there!")

say_hi()



# 3. Create a decorator to count how many times a function is called. 

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} to function: {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def welcome():
    print("Welcome!")

welcome()
welcome()
welcome()


# 4. Make a decorator that returns the square of the function's return value. 

def square_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

@square_output
def get_number():
    return 5

print(get_number()) 



# 5. Build a decorator that converts the return value of a function to uppercase. 

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_message():
    return "hello, world"

print(say_message())  


# 6. Write a decorator that logs the function’s arguments and return value. 

def log_args_return(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@log_args_return
def multiply(a, b):
    return a * b

multiply(4, 5)



# 7. Write a decorator to add logging before and after any function. 

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@logging_decorator
def process():
    print("Processing...")

process()


# 8. Create a decorator that adds exception handling to a function. 

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred: {e}")
    return wrapper

@exception_handler
def divide(x, y):
    return x / y

divide(10, 0) 



# 9. Build a decorator to print the execution time of a function. 

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def compute():
    time.sleep(1)
    return "Done"

compute()


# 10. Make a decorator that logs the current datetime before a function runs.

from datetime import datetime

def datetime_logger(func):
    def wrapper(*args, **kwargs):
        print("Current datetime:", datetime.now())
        return func(*args, **kwargs)
    return wrapper

@datetime_logger
def announce():
    print("Announcing the result...")

announce()

# Decorators with *args and **kwargs 

# 11. Create a decorator that accepts any number of arguments and logs them. 

def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def test(a, b, c=1):
    return a + b + c

test(1, 2, c=3)


# 12. Build a decorator that sums all arguments passed to a function. 

def sum_args(func):
    def wrapper(*args, **kwargs):
        print(f"Sum of all arguments: {sum(args)}")
        return func(*args, **kwargs)
    return wrapper

@sum_args
def add(a, b):
    return a + b

add(4, 6)


# 13. Make a decorator that validates the argument types using isinstance(). 

def validate_types(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, str)
def show(id, name):
    print(f"ID: {id}, Name: {name}")

show(1, "Alice")



# 14. Write a decorator that ensures a string argument is not empty. 

def non_empty_string(func):
    def wrapper(*args, **kwargs):
        if any(isinstance(arg, str) and not arg.strip() for arg in args):
            raise ValueError("String argument is empty!")
        return func(*args, **kwargs)
    return wrapper

@non_empty_string
def echo(message):
    print(message)

echo("Hello")



# 15. Write a decorator that enforces at least one keyword argument. 

def require_kwargs(func):
    def wrapper(*args, **kwargs):
        if not kwargs:
            raise ValueError("At least one keyword argument required.")
        return func(*args, **kwargs)
    return wrapper

@require_kwargs
def display(**kwargs):
    print(kwargs)

display(name="Nisha")



# 16. Create a decorator that only allows int arguments. 


def only_ints(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("All arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

@only_ints
def multiply(a, b):
    return a * b

print(multiply(3, 5))



# 17. Build a decorator that reverses a list argument before passing it to the function. 

def reverse_list_arg(func):
    def wrapper(lst, *args, **kwargs):
        if isinstance(lst, list):
            lst = lst[::-1]
        return func(lst, *args, **kwargs)
    return wrapper

@reverse_list_arg
def print_list(lst):
    print(lst)

print_list([1, 2, 3, 4])


# 18. Write a decorator that converts all string arguments to lowercase. 

def lowercase_args(func):
    def wrapper(*args, **kwargs):
        new_args = [arg.lower() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {k: v.lower() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

@lowercase_args
def greet(name):
    print(f"Hello {name}")

greet("NISHA")



# 19. Create a decorator that rounds float return values to 2 decimal places.   


def round_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            return round(result, 2)
        return result
    return wrapper

@round_return
def divide(a, b):
    return a / b

print(divide(10, 3))


# 20. Build a decorator that blocks function execution if a keyword block=True is  passed. 

def block_on_flag(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('block', False):
            print("Function execution blocked.")
            return None
        return func(*args, **kwargs)
    return wrapper

@block_on_flag
def send_message(msg):
    print(f"Sending: {msg}")

send_message("Hi", block=True)



# Decorators with Parameters (Decorator Factory) 

# 21. Create a decorator that repeats function output n times. 

def repeat_output(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_output(3)
def ring():
    print("Ding!")

ring()


# 22. Build a decorator that logs to a custom file path passed as an argument. 

def log_to_file(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(path, 'a') as f:
                f.write(f"Called {func.__name__} with {args}, {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_to_file("function_log.txt")
def hello(name):
    print(f"Hi, {name}")

hello("Nisha")


# 23. Create a decorator that limits how many times a function can be called. 

def call_limiter(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.calls >= limit:
                print("Call limit reached!")
                return
            wrapper.calls += 1
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator

@call_limiter(2)
def alert():
    print("Alert sent!")

alert()
alert()
alert()


# 24. Build a decorator that checks if a user has a specific role (e.g., admin, editor). 


def require_role(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') != role:
                raise PermissionError("Access Denied!")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def view_dashboard(user):
    print("Welcome Admin!")

view_dashboard({"name": "Nisha", "role": "admin"})


# 25. Write a decorator that enforces a minimum argument length. 

def min_arg_length(min_len):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) < min_len:
                raise ValueError("Insufficient arguments")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@min_arg_length(2)
def join_strings(a, b):
    return a + b

print(join_strings("Hi", "Nisha"))



# 26. Create a decorator that prints a custom prefix before every log. 

def log_with_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Executing {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_with_prefix("[LOG]")
def compute():
    print("Computing...")

compute()




# 27. Create a decorator that delays execution of the function by n seconds. 

import time

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Delaying for {seconds} second(s)...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(2)
def say_hi():
    print("Hi after delay!")

say_hi()



# 28. Create a decorator that adds a custom header and footer to printed output. 


def surround_output(header, footer):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator

@surround_output("-----START-----", "------END------")
def msg():
    print("Decorated Output")

msg()


# 29. Build a decorator that tracks time taken and prints a warning if it exceeds n seconds. 


import time

def time_warning(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            if duration > limit:
                print(f"Warning: Execution took {duration:.2f}s, exceeding {limit}s.")
            return result
        return wrapper
    return decorator

@time_warning(1)
def long_task():
    time.sleep(1.5)
    print("Finished task.")

long_task()


# 30. Write a decorator that applies a given function to the result of the  decorated function.


def apply_result(transform_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform_func(result)
        return wrapper
    return decorator

@apply_result(str.upper)
def get_name():
    return "nisha"

print(get_name())


# Multiple Decorators and Chaining 

# 31. Write two decorators: one to double the result and another to square it.  Chain them. 

def double_result(func):
    def wrapper(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return wrapper

def square_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@double_result
@square_result
def get_number():
    return 3

print(get_number())  # (3^2)*2 = 18


# 32. Create decorators @authenticate and @authorize, apply both to a function. 

def authenticate(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated", False):
            raise PermissionError("Not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

def authorize(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            raise PermissionError("Not authorized")
        return func(user, *args, **kwargs)
    return wrapper

@authenticate
@authorize
def access_dashboard(user):
    return "Dashboard Accessed"

user = {"authenticated": True, "role": "admin"}
print(access_dashboard(user))



# 33. Create @log_input, @log_output, and use both on a function. 

def log_input(func):
    def wrapper(*args, **kwargs):
        print(f"Input: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def log_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

@log_input
@log_output
def add(x, y):
    return x + y

add(4, 5)



# 34. Chain a decorator that reverses a string with one that uppercases it. 


def reverse_string(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)[::-1]
    return wrapper

def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@reverse_string
@uppercase
def message():
    return "hello"

print(message())  # OLLEH

# 35. Write two decorators: one that formats output in HTML <p> tags and  another in <div>. 

def html_p(func):
    def wrapper(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return wrapper

def html_div(func):
    def wrapper(*args, **kwargs):
        return f"<div>{func(*args, **kwargs)}</div>"
    return wrapper

@html_div
@html_p
def content():
    return "Hello World"

print(content())


# 36. Create a decorator chain for a CLI app: logging, timing, formatting. 


import time

def cli_log(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Starting...")
        return func(*args, **kwargs)
    return wrapper

def cli_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time taken: {time.time() - start:.2f}s")
        return result
    return wrapper

def cli_format(func):
    def wrapper(*args, **kwargs):
        return f">>> {func(*args, **kwargs)} <<<"
    return wrapper

@cli_log
@cli_time
@cli_format
def run_cli():
    time.sleep(1)
    return "Processing Done"

print(run_cli())



# 37. Build a mathematical chain: log the result, then check if it’s even. 

def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

def check_even(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Even" if result % 2 == 0 else "Odd")
        return result
    return wrapper

@log_result
@check_even
def compute():
    return 7

compute()



# 38. Make one decorator validate input, another one transform the result —  combine them. 


def validate_input(func):
    def wrapper(x):
        if not isinstance(x, int):
            raise ValueError("Only integers allowed")
        return func(x)
    return wrapper

def double_output(func):
    def wrapper(x):
        return func(x) * 2
    return wrapper

@validate_input
@double_output
def increment(x):
    return x + 1

print(increment(3))


# 39. Create a pipeline using multiple decorators that simulates processing stages. 

def stage1(func):
    def wrapper(*args, **kwargs):
        print("Stage 1")
        return func(*args, **kwargs)
    return wrapper

def stage2(func):
    def wrapper(*args, **kwargs):
        print("Stage 2")
        return func(*args, **kwargs)
    return wrapper

def stage3(func):
    def wrapper(*args, **kwargs):
        print("Stage 3")
        return func(*args, **kwargs)
    return wrapper

@stage1
@stage2
@stage3
def process():
    print("Processing...")

process()


# 40. Use functools.wraps to preserve function metadata when chaining. 

from functools import wraps

def preserve_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def original():
    """This is a test function."""
    return "Hello"

print(original.__name__)     # original
print(original.__doc__)      # This is a test function.


# Class-based Decorators and Built-in Types 

# 41. Implement a class-based decorator that logs before and after execution. 

class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before")
        result = self.func(*args, **kwargs)
        print("After")
        return result

@LogDecorator
def greet():
    print("Hi!")

greet()


# 42. Create a decorator that caches results (like memoization) using a class. 

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def slow_add(a, b):
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))  # Cached


# 43. Create a decorator class that tracks how many instances are created. 

class InstanceCounter:
    count = 0
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        InstanceCounter.count += 1
        print(f"Instances created: {InstanceCounter.count}")
        return self.cls(*args, **kwargs)

@InstanceCounter
class Person:
    def __init__(self, name):
        self.name = name

a = Person("A")
b = Person("B")


# 44. Decorate a class method with @classmethod, then wrap with your own  logger. 

def log_method(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Demo:
    @classmethod
    @log_method
    def info(cls):
        print("Class Method Called")

Demo.info()



# 45. Combine @property with a custom decorator to log when a property is accessed. 

def log_property(func):
    def wrapper(*args, **kwargs):
        print(f"Accessing property {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Product:
    def __init__(self, price):
        self._price = price

    @property
    @log_property
    def price(self):
        return self._price

item = Product(150)
print(item.price)


# Advanced Practical Decorators 

#46. Create a decorator that simulates API rate limiting (allow only 5 calls/min). 

import time

class RateLimit:
    def __init__(self, func):
        self.func = func
        self.calls = []

    def __call__(self, *args, **kwargs):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < 60]
        if len(self.calls) >= 5:
            raise Exception("Rate limit exceeded")
        self.calls.append(now)
        return self.func(*args, **kwargs)

@RateLimit
def fetch():
    print("Fetched data")

# Call fetch() 5 times quickly to see limit


# 47. Write a decorator for retrying a failed function up to 3 times. 

def retry(func):
    def wrapper(*args, **kwargs):
        for attempt in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {e}")
        print("All attempts failed.")
    return wrapper

@retry
def flaky():
    raise ValueError("Random failure")

flaky()



# 48. Implement a decorator to track time of each call and store in a log list. 

call_logs = []

def track_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        call_logs.append(duration)
        return result
    return wrapper

@track_time
def wait():
    time.sleep(0.5)

wait()
wait()
print(call_logs)


# 49. Build a security decorator that checks for a valid API token before  executing.


def check_token(func):
    def wrapper(*args, **kwargs):
        token = kwargs.get('token')
        if token != "SECRET123":
            raise PermissionError("Invalid API token")
        return func(*args, **kwargs)
    return wrapper

@check_token
def secure_action(**kwargs):
    print("Action allowed")

secure_action(token="SECRET123")

# 50. Create a decorator that encrypts and decrypts return values of functions  using a custom key. 

def encrypt_decrypt(key):
    def decorator(func):
        def wrapper(*args, **kwargs):
            raw = func(*args, **kwargs)
            encrypted = ''.join(chr(ord(c) ^ key) for c in raw)
            print("Encrypted:", encrypted)
            decrypted = ''.join(chr(ord(c) ^ key) for c in encrypted)
            print("Decrypted:", decrypted)
            return decrypted
        return wrapper
    return decorator

@encrypt_decrypt(5)
def secret_data():
    return "nisha"

secret_data()
