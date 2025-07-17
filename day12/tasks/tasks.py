# Section 1: Custom Modules

# 1. Create a simple module `math_tools.py` with add, subtract, multiply, and divide functions.

import math_tools
print(math_tools.add(2, 3))    
print(math_tools.divide(7, 2))   


# 2. Create a module `greetings.py` with a `greet_user(name)` function. Import it and greet different users.

from greetings import greet_user

greet_user("Alice")
greet_user("Bob")



# 3. Write a module `temperature_converter.py` to convert between Celsius and Fahrenheit.

import temperature_converter as tc

print(tc.c_to_f(0))    
print(tc.f_to_c(212))  




# 6. Use `from geometry import area` in another script and demonstrate selective import.

from geometry import area_circle

print(area_circle(3))  


# 7. Rename an imported function using `import geometry as geo` and use `geo.area()`.


import geometry as geo

print(geo.area_square(4))     
print(geo.perimeter_circle(2)) 



# 8. Split your math operations into `addition.py`, `subtraction.py`, etc. and import selectively.

from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

print(add(5, 2))       
print(subtract(5, 2))      
print(multiply(5, 2))  
print(divide(5, 2)) 

# 9. Use `__name__ == "__main__"` inside a module to run tests only when the file is executed directly.


if __name__ == "__main__":
    # Only runs when executed directly, not on import
    print("Testing math_tools module")
    assert add(2,3) == 5
    assert subtract(5,2) == 3
    print("All tests passed!")


# Section 2: Working with Built-in Modules

# 11. Use the `math` module to build a simple calculator that uses `sqrt()`, `pow()`, and `factorial()`.

import math

def sqrt(x):
    return math.sqrt(x)

def power(base, exp):
    return math.pow(base, exp)

def fact(n):
    return math.factorial(n)

if __name__ == "__main__":
    print(sqrt(16))   
    print(power(2, 3)) 
    print(fact(5))    



# 12. Create a game that uses the `random` module to generate a random number guessing game.

import random

def guessing_game():
    low, high = 1, 100
    secret = random.randint(low, high)
    attempts = 0

    print(f"Guess a number between {low} and {high}")

    while True:
        attempts += 1
        guess = int(input("Your guess: "))
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct in {attempts} attempts!")
            break

if __name__ == "__main__":
    guessing_game()



# 13. Use the `datetime` module to create a digital clock that prints the current time every second.


import datetime
import time

def digital_clock():
    try:
        while True:
            now = datetime.datetime.now()
            print(now.strftime("%H:%M:%S"), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    digital_clock()


# 14. Use the `calendar` module to display the calendar of the current month.

import calendar
from datetime import datetime

def show_current_month():
    now = datetime.now()
    print(calendar.month(now.year, now.month))

if __name__ == "__main__":
    show_current_month()



# 15. Use the `os` module to list all files in a given directory.

import os

def list_files(dir_path="."):
    for name in os.listdir(dir_path):
        print(name)

if __name__ == "__main__":
    list_files("/path/to/directory")



# 16. Create a script using `os.path` to check if a file exists before writing into it.

import os

filename = "example.txt"
if os.path.exists(filename):
    print(f"{filename} already exists.")
else:
    with open(filename, "w") as f:
        f.write("Hello, world!")
    print(f"{filename} created.")



# 17. Use the `platform` module to print OS, processor, and Python version.

import platform

def print_system_info():
    print("OS:", platform.system(), platform.release())
    print("Processor:", platform.processor())
    print("Python:", platform.python_version())

if __name__ == "__main__":
    print_system_info()



# 18. Use the `sys` module to access command-line arguments.

import sys

def main():
    print("Script name:", sys.argv[0])
    print("Arguments:", sys.argv[1:])

if __name__ == "__main__":
    main()



# 19. Use the `time` module to add a delay between prints using `time.sleep()`.

import time

for i in range(5):
    print(f"Step {i + 1}")
    time.sleep(1)
print("Done!")



# 20. Use the `statistics` module to calculate mean, median, and mode of a list of numbers.

import statistics

data = [2, 3, 5, 3, 2, 8, 3]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))

