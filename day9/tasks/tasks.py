# 🔹 1. Tuple Basics

#1.  Create an empty tuple and print its type.

t1 = ()
print(type(t1))


#2. Create a tuple with integers, strings, and a float and print each item.

t2 = (1, "hello", 3.14)
for item in t2:
    print(item)



#3. Create a tuple with only one element and print its type.

t3 = (5,)
print(type(t3))




#4. Convert a list of numbers [1, 2, 3, 4, 5] to a tuple.

lst = [1,2,3,4,5]
t4 = tuple(lst)
print(t4)



# 5. Convert the string "Python" into a tuple of characters.

t5 = tuple("Python")
print(t5)


# 🔹 2. Tuple Indexing and Slicing

# 6. Access the first and last elements of a tuple.

t = (10,20,30,40,50,60,70)
print(t[0], t[-1]) 


# 7. Slice a tuple to get the middle 3 elements.

print(t[2:5]) 


# 8. Reverse a tuple using slicing.

print(t[::-1]) 


# 9. Access every second element from a tuple using slicing.

print(t[::2])


# 10. Get a sub-tuple using negative indexing and slicing.

print(t[-5:-2])


# 🔹 3. Tuple Immutability

# 11. Attempt to change a tuple element and handle the resulting error.

t = (1,2,3)

# t[1] = 5  # ⇒ TypeError: 'tuple' object does not support item assignment



# 12. Show how to replace a value in a tuple by converting it to a list and back.

lst = list(t)
lst[1] = 99
t = tuple(lst)
print(t)



# 13.  Add a new value to a tuple (simulate by tuple concatenation).

t = t + (100,)
print(t)


# 14. Remove an item from a tuple (simulate by list conversion).

lst = list(t); lst.remove(3); t = tuple(lst)
print(t)

# 15. Demonstrate that tuples cannot be deleted partially (e.g., del tuple[0]).

# del t[0]  # ⇒ TypeError


# 🔹 4. Tuple Operations

# 16. Concatenate two tuples.

t1 = (1,2)
t2 = (3,4)

print(t1 + t2) 

# 17. Repeat a tuple 3 times using the * operator.

print(t1 * 3) 

# 18. Check if an item exists in a tuple using in.

print(2 in t1) 

# 19. Find the length of a tuple using len().

print(len(t2))

# 20. Count the number of times an element occurs in a tuple.

t3 = (1,2,1,3,1)
print(t3.count(1))


# 🔹 5. Tuple Functions and Methods

# 21. Use the count() method to count element occurrences.

t = (5,3,5,2,8,1,5)

print(t.count(5))


# 22. Use the index() method to find the position of an item.

print(t.index(8))


# 23. Use max() and min() on a tuple of numbers.

nums = (10,20,5,30)
print(max(nums), min(nums))


# 24. Use sum() to find the total of tuple items.

print(sum(nums))


# 25. Sort a tuple using sorted() (returns a list).
print(sorted(nums)) 


# 🔹 6. Iteration and Looping with Tuples

# 26. Iterate over a tuple using a for loop and print all elements.

t = (2,3,4,5,6,"Reetha","Nisha","Anna")

for x in t: 
    print(x)


# 27. Iterate with enumerate() to print index and value.

for i, x in enumerate(t):
    print(i, x)

# 28. Use a while loop to iterate through a tuple.

i=0
while i<len(t):
    print(t[i])
    i+=1


# 29. Print all even numbers from a tuple.

t = (2, 4, 6, 8)
for x in t:
    if x % 2 == 0:
        print(x)

# 30. Count how many strings start with “A” in a tuple of names.

t = ("Alice", "Bob", "Anna", "Charlie", "Andrew")

countA = 0
for name in t:
    if name.startswith("A"):
        countA += 1

print("Starts with A:", countA)



# 🔹 7. Nested Tuples

# 31.  Create a tuple of tuples and access inner elements.

nt = ((1,2),(3,4),(5,6))

# 32. Print all sub-tuples from a nested tuple.

for sub in nt:
    print(sub)            


# 33. Sum all numbers from a tuple of tuples like ((1,2), (3,4)).

tot = sum(a+b for a,b in nt)
print("Sum of all:", tot)


# 34. Flatten a nested tuple of integers using a loop.

flatten = [x for sub in nt for x in sub]
print(flatten)


# 35. Access the second element of the third sub-tuple.

print(nt[2][1])

# 🔹 8. Tuple Packing and Unpacking

# 36. Pack multiple values into a tuple and print.

t = 1,2,3
print(t)


# 37. Unpack a tuple into individual variables.

a,b,c = t
print(a,b,c)


# 38. Use unpacking to swap two variables.

x,y = 5,10
x,y = y,x
print(x,y)


# 39. Use * to unpack remaining values from a tuple.

t = (1,2,3,4,5)
a, *rest = t
print(a, rest)

# 40. Unpack nested tuples into individual values.
t = (1,(2,3),4)
a, (b,c), d = t
print(a,b,c,d)


# 🔹 9. Tuple Use in Functions

# 41. Write a function that returns multiple values as a tuple.
def get_stats(nums):
    """Return min, max, and average as a tuple."""
    minimum = min(nums)
    maximum = max(nums)
    avg = sum(nums) / len(nums)
    return minimum, maximum, avg  


stats = get_stats((10, 20, 30, 40))
print(stats)              
min_val, max_val, avg_val = get_stats((5,15,25))
print(min_val, max_val, avg_val)


# 42. Pass a tuple as an argument to a function and print elements.

def show_tuple(t):
    """Take a tuple, loop through and print each item."""
    for item in t:
        print(item)


my_tuple = ("apple", "banana", "cherry")
show_tuple(my_tuple)


# 43. Write a function to calculate average of numbers using tuple input.

avg = get_stats((5, 10, 15))[2]
print("Average:", avg)

# 44. Return both min and max from a tuple using a function.

def min_max(t):
    """Return a two-item tuple (min, max)."""
    return min(t), max(t)

a, b = min_max((3, 7, 2, 9))
print("Min:", a, "Max:", b)


# 45. Write a function to merge two tuples.

def merge_tuples(t1, t2):
    """Merge two tuples and return the result."""
    return t1 + t2


m1 = merge_tuples((1,2), ("a", "b"))
print(m1) 


# 🔹 10. Real-Life Tuple Applications

# 46. Store coordinates (latitude, longitude) as tuples and display them.

coords = (25.276987, 55.296249)
print("Coords:", coords)


# 47. Create a phone book with names and numbers stored as tuples in a list.

phonebook = [("Nisha","123"),("Reetha","456")]
for name, num in phonebook:
    print(name, num)


# 48. Represent RGB values of an image pixel using a tuple.

pixel = (255, 0, 128)
print("RGB:", pixel)

# 49. Store exam results (student_name, score) as tuples and print top scorer.

results = [("John",85),("Lina",92),("Joe",78)]
top = max(results, key=lambda x: x[1])
print("Top scorer:", top)


# 50. Use a tuple to represent an immutable configuration (host, port, debug_mode).

config = ("localhost", 8080, False)
host, port, debug = config
print(host, port, debug)