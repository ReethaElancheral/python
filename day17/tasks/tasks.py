# Basics of Generator Functions  


import sys
import os
import math

# 1. Create a generator function to yield numbers from 1 to 10. 

def gen_1_to_10():
    for i in range(1, 11):
        yield i

gen_1_to_10()

# 2. Write a generator to yield even numbers from 1 to n. 

def even_gen(n):
    for i in range(2, n+1, 2):
        yield i

even_gen(10)

# 3. Build a generator that yields squares of numbers from 1 to n. 

def square_gen(n):
    for i in range(1, n+1):
        yield i * i

square_gen(15)

# 4. Create a generator that yields characters from a given string. 

def char_gen(s):
    for ch in s:
        yield ch

print("4:", list(char_gen("Hello")))



# 5. Build a generator to yield all vowels from a string. 

def vowel_gen(s):
    vowels = 'aeiouAEIOU'
    for ch in s:
        if ch in vowels:
            yield ch

print("5:", list(vowel_gen("Generator")))


# 6. Use next() to manually iterate over a generator that yields the first 5 letters of the alphabet. 

def alphabet_gen():
    for ch in "ABCDE":
        yield ch

g = alphabet_gen()
print("6:", next(g), next(g), next(g), next(g), next(g))


# 7. Show how a generator stops when StopIteration is raised. 

def stop_gen():
    yield 1
    yield 2

try:
    g = stop_gen()
    print("7:", next(g), next(g), next(g))
except StopIteration:
    print("7: StopIteration reached")


# 8. Create a generator that yields prime numbers up to 100. 

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

def prime_gen():
    for i in range(2, 101):
        if is_prime(i):
            yield i

print("8:", list(prime_gen())[:10], "...")  # truncated

# 9. Compare a list-returning function vs generator (memory-wise) for 100000 elements. 

def list_return(n):
    return [i for i in range(n)]

def gen_return(n):
    for i in range(n):
        yield i

import sys
lst = list_return(100000)
gen = gen_return(100000)
print("9: List size:", sys.getsizeof(lst), "bytes | Generator size:", sys.getsizeof(gen), "bytes")

# 10. Create a generator that accepts a list and yields only positive numbers. 

def positive_only(lst):
    for num in lst:
        if num > 0:
            yield num

print("10:", list(positive_only([-2, 3, 0, 5, -1, 7])))


#  Intermediate Generator Logic  

# 11. Create a generator that yields words one-by-one from a paragraph. 

def word_gen(paragraph):
    for word in paragraph.split():
        yield word

print("11:", list(word_gen("Python is powerful and elegant")))

# 12. Create a generator that yields cumulative sum of a list of numbers. 

def cumulative_sum(lst):
    total = 0
    for num in lst:
        total += num
        yield total

print("12:", list(cumulative_sum([1, 2, 3, 4])))


# 13. Use yield with a for loop to re-implement range using a generator. 

def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

print("13:", list(my_range(1, 6)))


# 14. Create a generator that accepts a nested list and yields flattened values. 


def flatten(nested):
    for sub in nested:
        if isinstance(sub, list):
            yield from flatten(sub)
        else:
            yield sub

print("14:", list(flatten([[1, 2], [3, [4, 5]]])))

# 15. Build a generator that yields factorial of numbers up to n. 

def factorial_gen(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

print("15:", list(factorial_gen(5)))


# 16. Create a generator that yields powers of 2 up to a limit. 

def powers_of_two(limit):
    i = 1
    while i <= limit:
        yield 2 ** i
        i += 1

print("16:", list(powers_of_two(5)))



# 17. Generate Fibonacci sequence using a generator. 

def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("17:", list(fib_gen(8)))


# 18. Write a generator that filters and yields only even numbers from a list. 

def even_filter(lst):
    for i in lst:
        if i % 2 == 0:
            yield i

print("18:", list(even_filter([1, 2, 3, 4, 5, 6])))



# 19. Chain two generators together (e.g., one gives numbers, second squares them). 

def numbers():
    for i in range(1, 6):
        yield i

def squares(seq):
    for i in seq:
        yield i * i

print("19:", list(squares(numbers())))


# 20. Implement a reverse generator for a string. 

def reverse_gen(s):
    for i in reversed(s):
        yield i

print("20:", ''.join(reverse_gen("Python")))


#  Generator Expressions  

# 21. Create a generator expression to yield squares of numbers from 1 to 10. 

squares = (x*x for x in range(1, 11))
print("21:", list(squares))



#22. Write a generator expression to yield all odd numbers in a list. 

odds = (x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 1)
print("22:", list(odds))


# 23. Convert a generator expression into a list using list(). 

gen = (x for x in range(5))
print("23:", list(gen))



# 24. Create a generator expression to yield words longer than 5 characters in a  sentence. 

sentence = "Python generators are very efficient and useful"
long_words = (word for word in sentence.split() if len(word) > 5)
print("24:", list(long_words))

# 25. Use generator expression to yield uppercase letters from a string. 

upper = (ch for ch in "HelloWorld123" if ch.isupper())
print("25:", list(upper))

# 26. Compare generator expression vs list comprehension for large range. 

big_list = [i for i in range(1000000)]
big_gen = (i for i in range(1000000))
print("26: List size:", sys.getsizeof(big_list), "| Gen size:", sys.getsizeof(big_gen))

# 27. Use generator expression with sum() to calculate total. 

total = sum(x for x in range(1, 101))
print("27:", total)

# 28. Use a generator expression to filter floats from a mixed list. 

mixed = [1, 'a', 2.5, 3.1, 'x', 10]
floats = (x for x in mixed if isinstance(x, float))
print("28:", list(floats))


# 29. Use generator expression with any() to check if any number is divisible by 3. 

nums = [2, 4, 9, 11]
result = any(x % 3 == 0 for x in nums)
print("29:", result)

# 30. Use generator expression with max() to get the highest number.

values = [3, 7, 2, 8, 5]
max_val = max(x for x in values)
print("30:", max_val)

#  Advanced Generator Techniques  

# 31. Create an infinite generator that yields multiples of 5. 

def infinite_multiples_of_5():
    num = 5
    while True:
        yield num
        num += 5

gen = infinite_multiples_of_5()
for _ in range(5):
    print(next(gen))  # Output: 5, 10, 15, 20, 25



# 32. Create a generator that takes an iterable and chunks it into parts of 3. 

def chunk_generator(iterable, size=3):
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]

for chunk in chunk_generator([1, 2, 3, 4, 5, 6, 7]):
    print(chunk)  # Output: [1,2,3], [4,5,6], [7]



# 33. Create a generator that accepts a list of names and yields sorted names. 

def sorted_names(names):
    for name in sorted(names):
        yield name

for name in sorted_names(["Zara", "Anil", "Meera"]):
    print(name)  



#34. Yield reversed lines from a file using a generator. 

def reversed_lines(filename):
    with open(filename) as f:
        for line in reversed(f.readlines()):
            yield line.strip()

# Assuming file contains: Line1\nLine2\nLine3
# Output: Line3, Line2, Line1


# 35. Build a countdown generator that yields from n to 0. 

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # Output: 5, 4, 3, 2, 1, 0



# 36. Create a generator that logs yield points with a print statement. 

def log_generator():
    for i in range(3):
        print(f"Yielding {i}")
        yield i

for x in log_generator():
    pass
# Output: Yielding 0, Yielding 1, Yielding 2


# 37. Create a generator with send() that accepts external values and doubles them. 

def doubler():
    while True:
        val = yield
        print(val * 2)

g = doubler()
next(g)
g.send(10)  # Output: 20


# 38. Use return in a generator and handle StopIteration.value. 

def ret_gen():
    yield 1
    yield 2
    return "Done"

g = ret_gen()
try:
    while True:
        print(next(g))
except StopIteration as e:
    print(e.value)  # Output: Done



# 39. Create a CSV line reader using generator to yield one line at a time. 

def csv_reader(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip().split(',')

# Output: ['John', '25', 'IT'], ['Riya', '22', 'HR'], ...



# 40. Build a generator that tracks how many times yield is called. 

def counter_gen():
    count = 0
    for i in range(3):
        count += 1
        yield i
    print("Total yields:", count)

for x in counter_gen():
    print(x)
# Output: 0, 1, 2, Total yields: 3



#  Real-Life Generator Use Cases  

# 41. Build a log file reader generator that yields one log entry at a time. 

def log_reader(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()

# Output: Log line 1, Log line 2, ...


# 42. Simulate sensor data using a generator that yields values every 1 second. 


import time, random

def sensor_data():
    while True:
        yield random.randint(20, 40)
        time.sleep(1)

# Output: 24, wait, 28, wait, 35, ...


# 43. Use a generator to paginate API results (mocked). 

def paginate(items, per_page=2):
    for i in range(0, len(items), per_page):
        yield items[i:i+per_page]

api_data = [f"Item {i}" for i in range(1, 7)]
for page in paginate(api_data):
    print(page)
# Output: ['Item 1', 'Item 2'], ...



# 44. Create a streaming price monitor using generator for real-time stock prices. 

def price_monitor():
    while True:
        price = random.uniform(100, 200)
        yield round(price, 2)
        time.sleep(1)

# Output: 145.67, wait, 132.45, ...


# 45. Create a generator to simulate form validation results (e.g., each yield is a field check). 

def form_validator(fields):
    for field, is_valid in fields.items():
        yield f"{field}: {'Valid' if is_valid else 'Invalid'}"

for res in form_validator({'email': True, 'phone': False}):
    print(res)

# Output: email: Valid, phone: Invalid

#  Generator Comparison and Integration  

# 46. Compare list vs generator for iterating through 10 million numbers (benchmark). 

import time

def gen_large():
    for i in range(10000000):
        yield i

start = time.time()
for _ in gen_large():
    break
print("Generator:", time.time() - start)

start = time.time()
data = [i for i in range(10000000)]
print("List:", time.time() - start)
# Output: Generator < List


# 47. Integrate a generator with map() to transform each yielded value. 


def numbers():
    for i in range(5):
        yield i

squared = map(lambda x: x**2, numbers())
print(list(squared))  # Output: [0, 1, 4, 9, 16]


#  48. Create a generator pipeline: one yields numbers, second filters even, third   squares them. 

def nums():
    for i in range(10):
        yield i

def evens(gen):
    for i in gen:
        if i % 2 == 0:
            yield i

def squares(gen):
    for i in gen:
        yield i ** 2

result = squares(evens(nums()))
print(list(result))  # Output: [0, 4, 16, 36, 64]


# 49. Use generator in a for loop to simulate reading user input commands. 

def input_simulator(commands):
    for cmd in commands:
        yield cmd

for cmd in input_simulator(['start', 'stop', 'exit']):
    print(f"Command: {cmd}")
# Output: start, stop, exit


# 50. Write unit tests for a generator that returns only valid email addresses from  a list.

import re

def valid_emails(lst):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    for email in lst:
        if re.match(pattern, email):
            yield email

emails = ["abc@gmail.com", "wrong@.com", "xyz@domain.com"]
print(list(valid_emails(emails)))  # Output: ['abc@gmail.com', 'xyz@domain.com']


