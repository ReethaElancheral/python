# ✅ 📘 Basic Function Definition and Calling (1–10)

# Task 1: Define a function greet() that prints “Welcome to Python!”.
def greet():
    print("Welcome to Python!")
greet()

# Task 2: Write a function add(a, b) that returns the sum of two numbers.
def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", add(a, b))


# Task 3: Define a function is_even(num) that returns True if the number is even.
def is_even(num):
    return num % 2 == 0

n = int(input("Enter a number: "))
if is_even(n):
    print("Even number")
else:
    print("Odd number")


# Task 4: Create a function cube(n) that returns the cube of a number.
def cube(n):
    return n ** 3

n = int(input("Enter a number to find its cube: "))
print("Cube is:", cube(n))


# Task 5: Write a function hello(name) that prints "Hello, <name>".
def hello(name):
    print(f"Hello, {name}")

name = input("Enter your name: ")
hello(name)


# Task 6: Define a function with no code yet using pass.
def not_ready_yet():
    pass  

print("Function defined but not implemented.")


# Task 7: Create a function that takes two numbers and prints which is greater using if.
def greater(a, b):
    if a > b:
        print(f"{a} is greater")
    elif b > a:
        print(f"{b} is greater")
    else:
        print("Both numbers are equal")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
greater(x, y)


# Task 8: Write a function square_area(side) to return the area of a square.
def square_area(side):
    return side * side

side = float(input("Enter the side length of the square: "))
print("Area of square:", square_area(side))


# Task 9: Create a menu-based function with options (view, add, exit) using if-else.
def menu(choice):
    if choice == "view":
        print("Viewing data...")
    elif choice == "add":
        print("Adding data...")
    elif choice == "exit":
        print("Exiting program...")
    else:
        print("Invalid choice!")

choice = input("Enter your choice (view/add/exit): ").lower()
menu(choice)


# Task 10: Call a function multiple times in a loop to show reusability.
def greet_multiple():
    print("Welcome to Python!")

for i in range(3):
    greet_multiple()


# ✅ 📘 Functions with Parameters and Return Values (11–15)

# Task 11: Define a function divide(a, b) and return the quotient. Handle divide-by-zero.
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(10, 2)) 
print(divide(8, 0))   


# Task 12: Create a function full_name(fname, lname) that returns a full name.
def full_name(fname, lname):
    return fname + " " + lname

print(full_name("Nisha", "Reetha")) 


# Task 13: Write a function that takes age as input and returns if the user is eligible to vote.
def is_eligible_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

print(is_eligible_to_vote(20))  
print(is_eligible_to_vote(16))  


# Task 14: Create a function calc_discount(price, discount_percent) that returns the final price.
def calc_discount(price, discount_percent):
    discount = (price * discount_percent) / 100
    final_price = price - discount
    return final_price

print(calc_discount(1000, 10)) 


# Task 15: Write a function to calculate and return the average of 3 numbers.
def average_of_three(a, b, c):
    return (a + b + c) / 3

print(average_of_three(10, 20, 30)) 

# ✅ 📘 Global vs Local Variables (16–20)

# Task 16: Create a global variable x = 100, and print it inside a function.
x = 100 

def show_global():
    print("Global x inside function:", x)

show_global()
print("Global x outside function:", x)


# Task 17: Create a function with a local variable and show that it's not accessible outside.
def create_local():
    y = 50 
    print("Local y inside function:", y)

create_local()
# print(y) 



# Task 18: Use both a global and a local variable in the same function and print both.

num1 = 100 

def combine_scope():
    num2= 50  
    print("Global x:", num1)
    print("Local y:", num2)

combine_scope()


# Task 19: Modify a global variable inside a function using the global keyword.
count = 0 

def update_count():
    global count
    count += 1
    print("Updated global count:", count)

update_count()
print("Global count after function:", count)


# Task 20: Show that a variable with the same name inside a function doesn’t affect the global one.

name = "Nisha" 
def greet():
    name = "Mannavan"
    print("Inside function:", name)

greet()
print("Outside function:", name)

# ✅ 📘 Recursion Tasks (21–25)

# Task 21: Write a recursive function to calculate factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))


# Task 22: Create a recursive function to calculate the nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("7th Fibonacci number is:", fibonacci(7))


# Task 23: Use recursion to reverse a string.
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print("Reversed string:", reverse_string("Python"))


# Task 24: Use recursion to sum all elements in a list.
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

print("Sum of list:", list_sum([2, 4, 6, 8]))



# Task 25: Write a recursive function that counts down from a number to 1.

def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)


# ✅ 📘 *args and **kwargs Tasks (26–30)


# Task 26: Write a function add_numbers(*args) that returns the sum of all arguments.

def add_numbers(*args):
    return sum(args)

print(add_numbers(10, 20, 30))  

# Task 27: Create a function that prints all positional arguments received via *args.
def show_args(*args):
    for i, arg in enumerate(args, start=1):
        print(f"Arg {i}: {arg}")

show_args("Apple", "Banana", "Cherry")


# Task 28: Create a function student_info(**kwargs) to print student data.
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

student_info(name="Yazhs", age=13, grade="A")


# Task 29: Combine *args and **kwargs in one function and display both.
def mixed_args(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print("-", arg)

    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

mixed_args("Python", "Java", name="Mannavan", age=33)


# Task 30: Write a function that accepts an unknown number of keyword arguments and filters only those with integer values.

def filter_integers(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, int):
            print(f"{key}: {value}")

filter_integers(name="Nisha", age=25, score=88.5, passed=True, rank=1)


# ✅ 📘 Lambda Functions (31–35)

# Task 31: Write a lambda function to add two numbers.
add = lambda a, b: a + b
print(add(10, 5))  


# Task 32: Create a lambda to return the square of a number.
square = lambda num:num**2
print(square(15))

# Task 33: Use lambda with sorted() to sort a list of tuples by second value.
items = [("apple", 3), ("banana", 1), ("cherry", 2)]
sorted_items = sorted(items, key=lambda item: item[1])
print(sorted_items)



# Task 34: Replace a normal function with a lambda version.

# def multiply(x, y):
#     return x * y

multiply = lambda x, y: x * y
print(multiply(4, 5))  



# Task 35: Use a lambda function inside another function (function returning lambda).
def power_func(n):
    return lambda x: x ** n

square = power_func(2)
cube = power_func(3)

print(square(4)) 
print(cube(2))    

# ✅ 📘 Built-in Functions: map(), filter(), reduce() (36–40)

# Task 36: Use map() and lambda to square every element in a list.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  


# Task 37: Use filter() to remove all odd numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  


# Task 38: Use map() to convert a list of strings to uppercase.
words = ["python", "loop", "function"]
uppercase_words = list(map(lambda word: word.upper(), words))
print(uppercase_words) 


# Task 39: Use reduce() to calculate the product of a list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  


# Task 40: Use filter() to return words longer than 5 characters from a list.
words = ["hello", "python", "function", "if", "map"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  

# ✅ 📘 First-Class Functions (41–45)

# Task 41: Assign a function to a variable and call it using the new name.
def greet():
    print("Hello from Python!")

say_hello = greet

say_hello()  


# Task 42: Create a function that takes another function as an argument.
def upper(text):
    return text.upper()

def process(func):
    result = func("hello")
    print(result)

process(upper) 


# Task 43: Write a function that returns another function.
def greet_function(name):
    def inner():
        return f"Hello, {name}"
    return inner

greet_john = greet_function("John")
print(greet_john())  


# Task 44: Pass a lambda function as an argument to another function.
def apply_func(f, x):
    return f(x)

result = apply_func(lambda n: n * 2, 5)
print(result) 


# Task 45: Write a function that takes two numbers and a function (like add, subtract) and applies it.
def calculator(a, b, operation):
    return operation(a, b)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print(calculator(10, 5, add))    
print(calculator(10, 5, subtract)) 

# ✅ 📘 Inner Functions (46–47)

# Task 46: Write a function with a nested function inside that prints a message.

def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    
    inner_function()

outer_function()

# Task 47: Write a function that uses an inner function to double a number, and return the result.
def double_number(n):
    def inner():
        return n * 2
    
    return inner()

result = double_number(7)
print("Doubled:", result) 

# ✅ 📘 OOP: self and Class-based Function (48–49)

# Task 48: Create a class Person with attributes and a method greet() that uses self.
class Person:
    def __init__(self, name, age):
        self.name = name   
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Reetha", 33)
p1.greet() 


# Task 49: Create a class Calculator with methods add, subtract, using self.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
calc = Calculator()

print("Sum:", calc.add(10, 5))         
print("Difference:", calc.subtract(10, 5))  

# ✅ 📘 Bonus: Real-World Project-Based Function (50)

# Task 50: Create a billing app with functions:

# add_item(name, price)
# get_total()
# apply_discount(percent)
# Use *args, return, global variables, and lambda.


cart = []

def add_item(name, price):
    global cart
    cart.append((name, price))
    print(f"Added: {name} - ₹{price}")

def get_total():
    total = sum(price for _, price in cart)
    return total

def apply_discount(percent):
    total = get_total()
    discount_func = lambda amount: amount - (amount * percent / 100)
    final_amount = discount_func(total)
    return final_amount

add_item("Pen", 10)
add_item("Notebook", 50)
add_item("Bag", 500)

print("\nTotal without discount: ₹", get_total())
print("Total with 10% discount: ₹", apply_discount(10))
