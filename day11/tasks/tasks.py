# Creating and Accessing Sets

# 1. Create a set of favorite fruits and print it.

favorite_fruits = {"apple", "banana", "mango", "orange"}
print("1. Favorite fruits:", favorite_fruits)

# 2. Convert a list with duplicate values into a unique set.

dup_list = ["apple", "banana", "apple", "grape", "banana"]
unique_fruits = set(dup_list)
print("2. Unique fruits from list:", unique_fruits)

# 3. Check if a given item exists in a set using the in keyword.

item_to_check = "banana"
exists = item_to_check in favorite_fruits
print(f"3. Is '{item_to_check}' in favorite_fruits? ->", exists)

# 4. Create a set from a string and print all unique characters.

my_str = "hello world"
unique_chars = set(my_str)
print("4. Unique characters in string:", unique_chars)


# 5. Iterate through a set and print each element.

print(" Iterating through favorite_fruits:")
for fruit in favorite_fruits:
    print("-", fruit)

 
# Adding Elements

# 6. Create an empty set and add five movie names using add().

movies = set()
movies.add("Inception")
movies.add("The Matrix")
movies.add("Interstellar")
movies.add("The Godfather")
movies.add("Pulp Fiction")
print(" Movies set:", movies)

# 7. Add multiple subjects to a set using update() from a list.

subjects = {"Math", "History"}
more_subjects = ["Science", "Art", "Music"]
subjects.update(more_subjects)
print(" Subjects after update:", subjects)

# 8. Add multiple letters from a string into a set using update().

letters_set = set()
letters_set.update("python")
print(" Unique letters in 'python':", letters_set)
 
# Removing Elements

# 9. Remove a specific city from a set using remove().

cities = {"Paris", "London", "Tokyo", "New York"}
cities.remove("Tokyo")
print("9. Cities after removing Tokyo:", cities)

# 10. Try to remove an element using discard() and avoid an error if not present.

cities.discard("Berlin")  
print("10. Cities after discarding Berlin:", cities)

# 11. Remove a random item from a set using pop() and print it.

popped_city = cities.pop()
print("Popped random city:", popped_city)
print("Remaining cities:", cities)

# 12. Clear all elements from a set using clear() and check if it is empty.

cities.clear()
print("Cities after clear:", cities)
print("Is cities empty now?", len(cities) == 0)

# Set Operations

# 13. Find the union of two sets of programming languages.

langs1 = {"Python", "Java", "C++"}
langs2 = {"JavaScript", "Python", "Go"}
union_langs = langs1.union(langs2)
print("13. Union:", union_langs)

# 14. Find the intersection of two sets of sports.

sports1 = {"soccer", "tennis", "cricket"}
sports2 = {"rugby", "cricket", "basketball"}
intersection_sports = sports1.intersection(sports2)
print(" Intersection:", intersection_sports)

# 15. Find the difference between set A and set B (A - B).

difference_sports = sports1.difference(sports2)
print(f"Difference between sports are : {difference_sports}")

# 16. Find the symmetric difference (items in either set, but not both).

symmetric_sports = sports1.symmetric_difference(sports2)
print(f"symmeterci difference between sports are : {symmetric_sports}")


# 17. Perform chained operations like (A | B) - (A & B) on two sets. - symmetric difference

A = {1, 2, 3, 4}
B = {3, 4, 5}
chained = (A | B) - (A & B)
print("17. Chained (A|B)-(A&B):", chained)
 
# Set Relationships

# 18. Check if a set of backend skills is a subset of full-stack skills.

backend = {"Django", "Flask", "SQL"}
fullstack = {"Django", "Flask", "SQL", "React", "CSS"}
print("18. backend subset of fullstack?", backend.issubset(fullstack))


# 19. Verify if a set of developers is a superset of testers.

developers = {"Alice", "Bob", "Charlie"}
testers = {"Charlie", "Dave"}
print("19. developers superset of testers?", developers.issuperset(testers))

# 20. Determine if two sets of colors are disjoint (no common elements).

colors1 = {"red", "blue"}
colors2 = {"green", "yellow"}
print("20. Are colors disjoint?", colors1.isdisjoint(colors2))

# 21. Use multiple sets to test all subset-superset combinations.

X = {1, 2}
Y = {1, 2, 3}
Z = {2, 3}
print("21. X⊆Y?", X.issubset(Y))
print("21. Y⊇Z?", Y.issuperset(Z))
print("21. X⊇Z?", X.issuperset(Z))
print("21. Z⊆Y?", Z.issubset(Y))

# 22. Demonstrate a real-life case of issubset() using required course completions.

required = {"CS101", "CS102", "CS103"}
completed = {"CS101", "CS102", "CS103", "CS104"}
print("22. Completed required courses?", required.issubset(completed))
 
# Working with copy()

# 23. Create a backup of a set using copy() and show that modifying the copy doesn’t affect the original.

orig = {"apple", "banana"}
bak = orig.copy()
bak.add("cherry")
print("23. Original:", orig)
print("23. Copy after modification:", bak)
 
# Frozen Set Tasks

# 24. Create a frozenset of vowels and demonstrate immutability.

vowels = frozenset({"a", "e", "i", "o", "u"})
print("24. Vowels frozenset:", vowels)

# 25. Try to add an element to a frozenset and catch the error gracefully.
try:
    vowels.add("y")
except AttributeError as e:
    print("25. Cannot add to frozenset:", e)


# 26. Use a frozenset as a key in a dictionary for caching purposes.

cache = {}
fs_key = frozenset([1, 2, 3])
cache[fs_key] = "cached result"
print("26. cache with frozenset key:", cache)

# Set Comprehension

# 27. Generate a set of even numbers from 1 to 20 using set comprehension.

evens = {x for x in range(1, 21) if x % 2 == 0}
print("27.", evens)

# 28. Generate a set of unique lowercase characters from a sentence using set comprehension.
sentence = "Hello, World!"
unique_lower = {c for c in sentence if c.islower()}
print("28.", unique_lower)


# 29. Create a set of squares for numbers 1 to 10 using set comprehension.
squares = {x*x for x in range(1, 11)}
print("29.", squares)



# 30. Use a set comprehension to filter out vowels from a sentence.

vowels = set("aeiouAEIOU")
no_vowels = {c for c in sentence if c not in vowels}
print("30.", no_vowels)

 
# Real-World Simulations

# 31. Store a list of registered users and block users, then find the allowed users using set difference.

registered = {"alice", "bob", "carol", "dave"}
blocked = {"carol", "eve"}
allowed = registered - blocked
print("31. Allowed users:", allowed)


# 32. Use sets to find students enrolled in both Python and Java courses (intersection).

py = {"alice", "bob", "carol"}
java = {"bob", "dave"}
both = py.intersection(java) #py & java
print("32.", both)

# 33. Compare two sets of stock symbols to find new listings (difference).

old = {"AAPL", "GOOG", "MSFT"}
new = {"AAPL", "TSLA", "NVDA"}
new_listings = new.difference(old) #new - old
print("33.", new_listings)

# 34. Track users who logged in either yesterday or today (union).

yesterday = {"alice", "bob"}
today = {"carol", "alice"}
logged = yesterday.union(today) #yesterday | today
print("34.", logged)


# 35. Identify users who changed passwords on only one of the two days (symmetric difference).

pwd_changes = yesterday.symmetric_difference(today) #yesterday ^ today
print("35.", pwd_changes)

# 36. Detect duplicate entries in a list of product SKUs using sets.
skus = ["sku1", "sku2", "sku3", "sku2", "sku4", "sku1"]
duplicates = [s for s in set(skus) if skus.count(s) > 1]
print("36. Duplicates:", duplicates)


# 37. Create a set from a CSV file’s column and count unique entries.

import csv
with open("data.csv") as f:
    reader = csv.DictReader(f)
    col = {row["email"] for row in reader}
print("37.", f"Found {len(col)} unique emails.")

# 38. Build a unique tag manager system for blog posts using sets.

posts = [
  {"tags": ["python", "code", "tutorial"]},
  {"tags": ["code", "help"]},
]
tag_set = {tag for p in posts for tag in p["tags"]}
print("38.", tag_set)

# 39. Check if a given list of security permissions is covered by the default permission set.
 
default_perms = {"read", "write", "execute"}
user_perms = {"read", "write"}
print("39. Permissions covered?", user_perms.issubset(default_perms))



# Combination Tasks

# 40. Create two sets from random numbers and apply all operations: union, intersection, etc.

import random
A = set(random.sample(range(1,21), 7))
B = set(random.sample(range(1,21), 7))
print("40. A:", A)
print("40. B:", B)
print("union:", A|B, "intersection:", A&B, "diff(A,B):", A-B, "sym_diff:", A^B)


# 41. Build a contact manager that stores unique email addresses using a set.

contacts = set()
for e in ["a@example.com", "b@example.com", "a@example.com"]:
    contacts.add(e)
print("41. Unique contacts:", contacts)

# 42. Store completed achievements of players and check who earned all major trophies.

needed = {"trophy1", "trophy2", "trophy3"}
player = {"trophy1", "trophy2"}
print("42. All trophies earned?", needed.issubset(player))

# 43. Keep track of unique IPs from a server log using a set.

ips = set()
with open("access.log") as f:
    for line in f:
        ips.add(line.split()[0])
print("43. Unique IP count:", len(ips))

# 44. Extract unique hashtags from a list of tweets using sets.

tweets = ["Love #python", "Coding in #python #dev"]
hashtags = {tag for t in tweets for tag in t.split() if tag.startswith("#")}
print("44.", hashtags)

# 45. Track unique book titles from multiple libraries using update().

lib1 = {"Book A", "Book B"}
lib2 = {"Book B", "Book C"}
all_books = set()
all_books.update(lib1, lib2)
print("45.", all_books)

# 46. Validate if all required modules are installed using issubset() on installed_modules.

installed = {"numpy", "pandas", "requests"}
required = {"numpy", "requests"}
print("46. Installed covers required?", required.issubset(installed))

# Edge Case Handling

# 47. Try removing a non-existent item using remove() and handle the exception.

s = {"apple", "banana", "cherry"}
try:
    s.remove("orange")
except KeyError as e:
    print("47. remove() error caught:", e)
print("   Current set:", s)

# 48. Explain the difference between remove() and discard() using a test set.

s2 = {"a", "b", "c"}
# discard non-existent
s2.discard("d")
print("48. After discard('d'):", s2)
# remove non-existent with try
try:
    s2.remove("d")
except KeyError:
    print("   remove('d') raised KeyError")
print("   Final set:", s2)


# 49. Create a set from a list with mixed datatypes and remove all integers using set comprehension.


mixed = [1, "1", 2, "a", 3.0, 4]
mixed_set = set(mixed)
filtered = {x for x in mixed_set if not isinstance(x, int)}
print("49. Filtered set (no ints):", filtered)

# 50. Create a set of characters from a multiline text, excluding punctuation.

import string

text = """Hello, World!
This is a test.
"""
chars = {
    c.lower()
    for c in text
    if c not in string.punctuation and not c.isspace()
}
print("50. Unique letters from text:", chars)
