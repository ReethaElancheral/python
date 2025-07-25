# Basic Iterator and Iterable Understanding  

# 1. Use iter() and next() to iterate over a list manually. 

numbers = [10, 20, 30, 40, 50]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# 2. Use a for loop vs while with next() to iterate a tuple. 

tup = ('a', 'b', 'c')

# Using for loop
print("Using for loop:")
for item in tup:
    print(item)

# Using while loop with next()
print("\nUsing while loop with next():")
it = iter(tup)
while True:
    try:
        print(next(it))
    except StopIteration:
        break


# 3. Create a program to check if a variable is iterable using dir(). 

def is_iterable(obj):
    return '__iter__' in dir(obj)

print(is_iterable([1, 2, 3]))    
print(is_iterable(123))          
print(is_iterable("hello"))     


# 4. Try to use next() on a non-iterator and handle the exception. 

num = 100
try:
    print(next(num))  # int is not an iterator
except TypeError as e:
    print("Error:", e)


# 5. Write a program to manually consume only the first 3 elements of a set. 

my_set = {10, 20, 30, 40, 50}
it = iter(my_set)

print(next(it))
print(next(it))
print(next(it))



# 6. Use next() to iterate through characters in a string. 

text = "Python"
it = iter(text)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



# 7. Use iter() on a dictionary and fetch only the keys. 

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Pune'}
key_iter = iter(my_dict)

print(next(key_iter))
print(next(key_iter))
print(next(key_iter))



# 8. Convert a range object to an iterator and loop using next(). 

r = range(5)
it = iter(r)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



# 9. Write a function that takes an iterable and prints each item using next(). 


def print_iterable(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

print_iterable([1, 2, 3, 4])



# 10. Handle StopIteration with a try-except block after consuming all items. 

lst = ['x', 'y', 'z']
it = iter(lst)

try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))  # This will raise StopIteration
except StopIteration:
    print("Reached end of iterator.")

# Custom Iterator Classes  

# 11. Create a class Countdown that counts down from a number using __iter__()  and __next__(). 

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)




# 12. Create a custom iterator EvenNumbers that yields only even numbers up to  n. 

class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                val = self.current
                self.current += 1
                return val
            self.current += 1
        raise StopIteration

for even in EvenNumbers(10):
    print(even)



# 13. Build a class CharIterator that iterates over characters in a string. 

class CharIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        self.index += 1
        return char

for ch in CharIterator("hello"):
    print(ch)


# 14. Create FibonacciIterator that generates Fibonacci numbers up to n. 

class FibonacciIterator:
    def __init__(self, limit):
        self.a, self.b = 0, 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

for fib in FibonacciIterator(50):
    print(fib)


# 15. Build ReverseListIterator to yield items of a list in reverse order. 

class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        val = self.data[self.index]
        self.index -= 1
        return val

for item in ReverseListIterator([1, 2, 3, 4]):
    print(item)


# 16. Write SquareIterator to yield squares of numbers in a range. 

class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current ** 2
        self.current += 1
        return val

for sq in SquareIterator(1, 5):
    print(sq)


# 17. Create a LetterPositionIterator that returns (letter, position) from a string. 

class LetterPositionIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        pair = (self.text[self.index], self.index)
        self.index += 1
        return pair

for item in LetterPositionIterator("abcde"):
    print(item)



# 18. Create CountdownWithStop that stops early based on a condition. 

class CountdownWithStop:
    def __init__(self, start, stop_at):
        self.current = start
        self.stop_at = stop_at

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_at:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for val in CountdownWithStop(10, 5):
    print(val)



# 19. Create an iterator that yields vowels from a sentence. 

class VowelIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.vowels = 'aeiouAEIOU'

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            ch = self.text[self.index]
            self.index += 1
            if ch in self.vowels:
                return ch
        raise StopIteration

for v in VowelIterator("Beautiful Day"):
    print(v)



# 20. Create an iterator that returns digits from a mixed string. 

class DigitIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            ch = self.text[self.index]
            self.index += 1
            if ch.isdigit():
                return ch
        raise StopIteration

for d in DigitIterator("a1b2c3x"):
    print(d)


#  Advanced Use of iter()  

# 21. Use iter(callable, sentinel) to read lines from input until "exit". 

for line in iter(input, "exit"):
    print(f"Received: {line}")



# 22. Implement a custom file reader using iter() and a sentinel value. 

with open("sample.txt") as f:
    for line in iter(f.readline, ''):
        print(line.strip())


# 23. Write a loop that fetches random numbers until a number > 90 is generated. 

import random

for num in iter(lambda: random.randint(1, 100), 91):
    print(num)
    if num > 90:
        break


# 24. Write a generator-less iterator using iter() that stops when 0 is entered. 

def read_until_zero():
    return int(input("Enter number: "))

for val in iter(read_until_zero, 0):
    print(f"Got: {val}")



# 25. Create an iterator to filter out all non-alphabet characters. 

text = "He11o W0rld!"
alpha_iter = (ch for ch in text if ch.isalpha())

for ch in alpha_iter:
    print(ch)


# 26. Use iter() with a lambda to simulate infinite number stream. 

counter = iter(lambda: random.randint(1, 10), None)
for _ in range(5):
    print(next(counter))


# 27. Build a calculator input stream using iter(input, “done”). 

for expr in iter(input, "done"):
    try:
        print("Result:", eval(expr))
    except:
        print("Invalid expression.")


# 28. Create a lazy square root generator using math.sqrt and iter(). 

import math

nums = [4, 9, 16, 25]
sqrt_iter = iter(map(math.sqrt, nums))
for s in sqrt_iter:
    print(s)



# 29. Write a program that takes any iterable and iterates using iter() with next() and index. 

def iterate_with_index(data):
    it = iter(data)
    idx = 0
    while True:
        try:
            print(f"{idx}: {next(it)}")
            idx += 1
        except StopIteration:
            break

iterate_with_index(['a', 'b', 'c'])


# 30. Use iter() with a stop-signal and display how many times it looped. 

count = 0
for val in iter(input, "stop"):
    print(val)
    count += 1
print("Looped:", count, "times")


#  Iterator with Files  

# 31. Open a file and use iter() to read line-by-line using next(). 

with open("sample.txt") as f:
    it = iter(f)
    print(next(it))
    print(next(it))


# 32. Handle StopIteration when reaching the end of a file manually. 

with open("sample.txt") as f:
    it = iter(f)
    while True:
        try:
            print(next(it).strip())
        except StopIteration:
            break


# 33. Create a custom file iterator that only returns non-empty lines. 

class NonEmptyLineIterator:
    def __init__(self, filepath):
        self.file = open(filepath)

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            if line.strip():
                return line.strip()
        self.file.close()
        raise StopIteration

for line in NonEmptyLineIterator("sample.txt"):
    print(line)




# 34. Build an iterator that returns the first word of each line in a file. 

with open("sample.txt") as f:
    for line in f:
        words = line.strip().split()
        if words:
            print(words[0])



# 35. Create a program that returns lines with more than 3 words using iterators. 

with open("sample.txt") as f:
    for line in f:
        words = line.strip().split()
        if len(words) > 3:
            print(line.strip())


#  Loop Integration and Comparison  

#36. Compare performance of for loop vs while next() for large list. 

import time

data = list(range(100000))

start = time.time()
for item in data:
    _ = item
print("For loop:", time.time() - start)

start = time.time()
it = iter(data)
while True:
    try:
        _ = next(it)
    except StopIteration:
        break
print("While-next loop:", time.time() - start)


# 37. Write an iterator that can skip alternate items. 

class SkipIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 2
        return val

for val in SkipIterator([1, 2, 3, 4, 5, 6]):
    print(val)




# 38. Write an iterator to loop over two iterables at once (like zip()). 

class ZipLike:
    def __init__(self, a, b):
        self.it1 = iter(a)
        self.it2 = iter(b)

    def __iter__(self):
        return self

    def __next__(self):
        return (next(self.it1), next(self.it2))

for pair in ZipLike([1, 2, 3], ['a', 'b', 'c']):
    print(pair)


# 39. Create a reusable class that wraps a list and gives peekable iterator. 

class PeekableIterator:
    def __init__(self, data):
        self.data = iter(data)
        self._cache = None
        self._peeked = False

    def peek(self):
        if not self._peeked:
            self._cache = next(self.data)
            self._peeked = True
        return self._cache

    def __next__(self):
        if self._peeked:
            self._peeked = False
            return self._cache
        return next(self.data)

    def __iter__(self):
        return self

it = PeekableIterator([10, 20, 30])
print("Peek:", it.peek())
print("Next:", next(it))


# 40. Simulate circular iteration over a list (restarts after end). 

class CircularIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return val

circ = CircularIterator([1, 2, 3])
for _ in range(7):
    print(next(circ))


#  Exception Handling and Edge Cases  

# 41. Use a try-except block to catch StopIteration and continue a new list. 

a = iter([1, 2])
b = iter([3, 4])

try:
    while True:
        print(next(a))
except StopIteration:
    for i in b:
        print(i)


# 42. Build an iterator that raises a custom error after 5 items.

class LimitIterator:
    def __init__(self, data):
        self.data = data
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 5:
            raise Exception("Limit exceeded")
        val = self.data[self.count]
        self.count += 1
        return val

for item in LimitIterator([1, 2, 3, 4, 5, 6, 7]):
    print(item)


# 43. Modify __next__() to raise StopIteration with custom message. 

class CustomStopIterator:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 3:
            raise StopIteration("No more items!")
        self.count += 1
        return self.count

it = CustomStopIterator()
try:
    while True:
        print(next(it))
except StopIteration as e:
    print(e)


# 44. Write a safe iterator that silently ends without exception using a wrapper. 

def safe_iter(it):
    try:
        return next(it)
    except StopIteration:
        return None

lst = iter([1, 2])
print(safe_iter(lst))
print(safe_iter(lst))
print(safe_iter(lst))  # None


# 45. Create an iterator that prints a warning before stopping. 

class WarningIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            print("Warning: Iterator ending!")
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val

for val in WarningIterator([1, 2]):
    print(val)


#  Real-Life Use Case Based Iterators  

# 46. Create a PaginationIterator for navigating list of blog articles page-by-page. 

class PaginationIterator:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        page = self.items[self.index:self.index + self.page_size]
        self.index += self.page_size
        return page

posts = [f"Post {i}" for i in range(1, 11)]
for page in PaginationIterator(posts, 3):
    print(page)



# 47. Build a TransactionIterator that returns 5 transactions at a time. 

class TransactionIterator:
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.transactions):
            raise StopIteration
        batch = self.transactions[self.index:self.index+5]
        self.index += 5
        return batch

tx = [f"TX-{i}" for i in range(12)]
for group in TransactionIterator(tx):
    print(group)


# 48. Build a SensorDataIterator that stops reading when a threshold is breached. 

class SensorDataIterator:
    def __init__(self, readings, threshold):
        self.readings = readings
        self.threshold = threshold
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.readings) or self.readings[self.index] > self.threshold:
            raise StopIteration
        val = self.readings[self.index]
        self.index += 1
        return val

data = [20, 30, 40, 95, 50]
for r in SensorDataIterator(data, 90):
    print(r)


# 49. Design EmailValidatorIterator that yields only valid emails from a list. 

import re

class EmailValidatorIterator:
    def __init__(self, emails):
        self.emails = emails
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.emails):
            email = self.emails[self.index]
            self.index += 1
            if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                return email
        raise StopIteration

emails = ["test@example.com", "invalid@", "name@domain.com"]
for e in EmailValidatorIterator(emails):
    print(e)



# 50. Create a ProductStockIterator that yields products below threshold level.

class ProductStockIterator:
    def __init__(self, products, threshold):
        self.products = products
        self.threshold = threshold
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.products):
            name, qty = self.products[self.index]
            self.index += 1
            if qty < self.threshold:
                return (name, qty)
        raise StopIteration

items = [("Pen", 50), ("Pencil", 5), ("Notebook", 2)]
for p in ProductStockIterator(items, 10):
    print(p)
