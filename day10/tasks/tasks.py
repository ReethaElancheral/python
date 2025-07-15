# 1. Create employee dict with name→ID
employees = {"Alice": 101, "Bob": 102, "Cara": 103, "David": 104, "Eva": 105}

# 2. Access phone number
contacts = {"Alice": "555-1234", "Bob": "555-5678"}
print("Bob’s phone:", contacts["Bob"])

# 3. Use get() safely
print("Eve’s phone:", contacts.get("Eve", "Not Found"))

# 4. Add to student marks
marks = {"Alice": 85, "Bob": 78}
marks["Cara"] = 92

# 5. Update existing student's score
marks["Bob"] = 88

# 6. Delete a key
del marks["Alice"]

# 7. Pop key and show returned value
grade = marks.pop("Cara")
print("Removed Cara’s grade:", grade)

# 8. popitem()
last = marks.popitem()
print("Popped item:", last)
# Explanation: popitem() removes and returns the last inserted key-value pair

# 9. clear()
marks.clear()
print("Marks after clear:", marks)

# 10. Check if a key exists
print("Bob in marks?", "Bob" in marks)

scores = {"Alice":95, "Bob":82, "Cara":90, "David":78}

# 11. Print keys
for k in scores:
    print(k)

# 12. Print values
for v in scores.values():
    print(v)

# 13. Print items
for k, v in scores.items():
    print(k, v)

# 14. Count values > 90
count = sum(1 for v in scores.values() if v > 90)
print("Scores above 90:", count)

# 15. Function to get keys with specific value
def keys_with_value(d, target):
    return [k for k, v in d.items() if v == target]
print("Keys with score 82:", keys_with_value(scores, 82))


dict1 = {"a":1, "b":2}
dict2 = {"b":3, "c":4}

# 16. update()
dict1.update(dict2)  # now dict1 = {'a':1,'b':3,'c':4}

# 17. setdefault()
dict1.setdefault("d", 5)  # adds 'd':5 only if missing

# 18. copy()
d_copy = dict1.copy()
dict1["a"] = 99
print("Original:", dict1, "Copy:", d_copy)

# 19. dict() constructor from list of tuples
pairs = [("x", 24), ("y", 25)]
d3 = dict(pairs)

# 20. keys() and values()
keys = list(d3.keys())
vals = list(d3.values())
print("Keys:", keys, "Values:", vals)

# 21. Shopping cart: item→qty
cart = {"apple":2, "bread":1}

# 22. Grade book: student→grade
grades = {"Alice":"A", "Bob":"B+"}

# 23. Phonebook
phonebook = {"Alice":"555-1234", "Bob":"555-5678"}
print("Search Alice:", phonebook.get("Alice", "Not found"))

# 24. Product inventory: ID→stock
inventory = {1001:50, 1002:20}

# 25. Attendance: date→list of students
attendance = {"2025-07-14":["Alice","Bob"]}

# 26. Nested employee dict
employees = {101:{"name":"Alice","salary":5000}, 102:{"name":"Bob","salary":4500}}

# 27. Access nested value
print("Bob's salary:", employees[102]["salary"])

# 28. Add employee
employees[103] = {"name":"Cara","salary":4800}

# 29. Update salary
employees[102]["salary"] = 4600

# 30. Loop through nested dict
for emp_id, info in employees.items():
    print(f"ID: {emp_id}, Name: {info['name']}, Salary: {info['salary']}")

# 31. Squares dict
squares = {n: n**2 for n in range(1,6)}

# 32. Even/odd mapping
nums = [1,2,3,4]
parity = {n: ("even" if n%2==0 else "odd") for n in nums}

# 33. Words→length
words = ["apple","banana"]
lengths = {w: len(w) for w in words}

# 34. Swap keys and values
orig = {"a":1, "b":2}
swapped = {v:k for k,v in orig.items()}

# 35. Filter values > threshold
scores = {"a":50,"b":95,"c":85}
high = {k:v for k,v in scores.items() if v>90}

# 36. Character frequency
text = "hello"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# 37. Word count from paragraph
para = "hello world hello"
wc = {}
for w in para.split():
    wc[w] = wc.get(w, 0) + 1

# 38. Fruit prices, find most expensive
fruits = {"apple":1.2, "banana":0.8, "cherry":2.5}
exp = max(fruits, key=fruits.get)
print("Most expensive fruit:", exp)

# 39. Inventory value
prices = {"pen":1.5,"book":5}
qty = {"pen":10,"book":3}
total = sum(prices[i]*qty.get(i,0) for i in prices)

# 40. Group students by grade
student_grades = [("Alice","A"),("Bob","B"),("Cara","A")]
groups = {}
for name, grade in student_grades:
    groups.setdefault(grade, []).append(name)

# 41. Implement a caching system using a dictionary to store function results.

cache = {}

def cache_function(func):
    def wrapper(arg):
        if arg in cache:
            print("✔️ Retrieved from cache")
            return cache[arg]
        result = func(arg)
        cache[arg] = result
        return result
    return wrapper

@cache_function
def expensive_calc(n):
    print("Calculating...")
    return n * n

# Usage
print(expensive_calc(10))
print(expensive_calc(10))  

# 42. URL shortener using dict

import hashlib

class URLShortener:
    def __init__(self):
        self.map = {}
        self.base = "http://short.ly/"

    def shorten(self, long_url):
        code = hashlib.md5(long_url.encode()).hexdigest()[:6]
        short_url = self.base + code
        self.map[short_url] = long_url
        return short_url

    def expand(self, short_url):
        return self.map.get(short_url)

# Example
srv = URLShortener()
s = srv.shorten("https://example.com/very/long/url")
print(s, "->", srv.expand(s))


# 43. Simple translator dict

translator = {
    "hello": "வணக்கம்",
    "thank you": "நன்றி",
    "yes": "ஆம்",
    "no": "இல்லை"
}

def translate_en_to_ta(word):
    return translator.get(word.lower(), "பெயரில்லை")  


print(translate_en_to_ta("Hello"))
print(translate_en_to_ta("Yes"))
print(translate_en_to_ta("Goodbye"))


# 44. Login system using dict

users = {
    "alice": "alice123",
    "bob": "bob456",
    "cara": "cara789"
}

def login(username, password):
    stored = users.get(username)
    if stored and stored == password:
        return True
    return False


print("Login alice:", login("alice", "alice123"))
print("Login bob:", login("bob", "wrong"))


# Utility Tools

# 46. Create a dictionary-based simple calculator (keys as operators and values as functions).

import operator

calc = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def simple_calc(a, b, op):
    if op in calc:
        return calc[op](a, b)
    else:
        print("Unsupported operator")
        return None


print("5 + 3 =", simple_calc(5, 3, '+'))



# 47. Build a travel expense tracker using a dictionary where destinations are keys and costs are values.

expenses = {} 

def add_expense(destination, cost):
    expenses[destination] = expenses.get(destination, 0) + cost

add_expense("Dubai", 200)
add_expense("Paris", 450)
add_expense("Dubai", 150)

print("Travel expenses:", expenses)



# 48. Develop a file extension counter: count how many files per extension from a list of filenames.

import os
from collections import Counter

def ext_counter(folder_path):
    exts = [
        os.path.splitext(f)[1].lower()
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    return Counter(exts)

Counter({'.txt': 5, '.jpg': 3})

# 49. Build a dictionary that maps countries to their capital cities and allow searching.


capitals = {
    "Qatar": "Doha",
    "France": "Paris",
    "Japan": "Tokyo"
}

def get_capital(country):
    return capitals.get(country, "Unknown country")

print("Capital of Japan:", get_capital("Japan"))
print("Capital of Egypt:", get_capital("Egypt"))


# 50. Create a quiz app using dictionaries: {question: correct_option} and verify answers.
quiz = {
    "What is 2+2?": "4",
    "Capital of France?": "Paris",
    "Python keyword for function?": "def"
}

def take_quiz(qdict):
    score = 0
    for q, correct in qdict.items():
        ans = input(q + " ")
        if ans.strip() == correct:
            score += 1
    print(f"Your score: {score}/{len(qdict)}")


take_quiz(quiz)
