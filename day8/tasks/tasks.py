# List Creation & Basic Operations (Tasks 1–10)

# 1. Create a list of 5 student names and print it.

student_names = ['Nisha','Reetha','Karthiga','Mannavan', 'Lakshitha']
print(f"Students Names: {student_names}")


# 2. Create a list with mixed data types (int, float, string, bool) and display each element.

mixed_list = [25, 3.14, "Python", True]
print("\nMixed List Elements:")
for item in mixed_list:
    print(item)



# 3. Write a program to accept 5 numbers from the user and store them in a list.

user_numbers = []
print("\nEnter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    user_numbers.append(num)
print("User Numbers:", user_numbers)


# 4. Create an empty list and dynamically append 3 user inputs.

dynamic_list = []
print("\nEnter 3 items to append to the list:")
for i in range(3):
    item = input(f"Item {i+1}: ")
    dynamic_list.append(item)
print("Dynamic List:", dynamic_list)


# 5. Write a program to create a list of 10 even numbers using a for loop.

even_numbers = []
for i in range(2, 21, 2):
    even_numbers.append(i)
print("Even Numbers:", even_numbers)

# 6. Create two lists, one with integers and one with strings, then print them together.

int_list = [1, 2, 3]
str_list = ["one", "two", "three"]
new_list = int_list + str_list
print("New List:", new_list)



# 7. Create a list of fruits and print only the first and last items using indexing.

fruits = ["apple", "banana", "cherry", "date", "blackberry"]
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])


# 8. Use negative indexing to print the second-last item in a list.

print("Second-last Fruit:", fruits[-2])

# 9. Write a program to count the total number of elements in a list using len().

print("Number of Fruits:", len(fruits))

# 10. Check and print the data type of a created list.

print("Data type of 'fruits' list:", type(fruits))

# Accessing & Indexing Tasks (11–15)

# 11. Access and print each element of a list using a for loop with indexing.

colors = ["red", "green", "blue", "yellow", "purple"]
print("Colors (by index):")
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")


# 12. Print every alternate item from a list using slicing.

print("Alternate Colors:", colors[::2])

# 13. Create a list of cities and print the third character of the second city.

cities = ["Doha", "London", "Tokyo", "Paris"]
print("Third character of second city:", cities[1][2])  

# 14. Write a program to reverse a list using slicing.

reversed_colors = colors[::-1]
print("Reversed Colors List:", reversed_colors)


# 15. Access the last element of a list using both positive and negative indexing.

cities = ["Doha", "London", "Tokyo", "Paris"]
print("Last City (positive index):", cities[3])
print("Last City (negative index):", cities[-1])



# ✅ Adding Elements to Lists (Tasks 16–20)

# 16. Start with an empty list and use append() to add 5 elements.

numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)
print("Numbers after append():", numbers)

# 17. Insert an element at the 3rd position in a list.
 
numbers.insert(2, 25)  
print("After insert at 3rd position:", numbers)


# 18. Use extend() to add multiple elements to an existing list.

more_numbers = [60, 70, 80]
numbers.extend(more_numbers)
print("After extend():", numbers)


# 19. Take user input for a name and add it to an existing list of students.

students = ["Reetha", "Geetha", "Karthiga"]
new_name = input("Enter a new student name: ")
students.append(new_name)
print("Updated Students List:", students)


# 20. Add all elements from one list into another using += and extend().

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using +=
combined1 = list1.copy()
combined1 += list2
print("\nList after += :", combined1)

# Using extend()
combined2 = list1.copy()
combined2.extend(list2)
print("List after extend():", combined2)

# Updating List Items (Tasks 21–25)

# 21. Change the first element of a list to uppercase.

names = ["reetha", "geetha", "nisha"]
names[0] = names[0].upper()
print("Updated names list:", names)



# 22. Modify the price of a product in a list of prices (e.g., change index 2 value to 999).

prices = [199, 299, 399, 499]
prices[2] = 999
print("Updated prices:", prices)



# 23. Update all odd numbers in a list by multiplying them by 2.

numbers = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] *= 2
print("Odd numbers doubled:", numbers)


# 24. Write a program to replace a fruit in a list with a new fruit.

fruits = ["apple", "banana", "cherry", "date"]
fruits[1] = "mango"  
print("Updated fruits list:", fruits)


# 25. Update the value of a nested list item (list[1][2] = 'done').

nested = [[1, 2], [3, 4, 5], [6, 7]]
nested[1][2] = "done"
print("Updated nested list:", nested)


# Removing Elements (Tasks 26–30)

# 26. Use remove() to delete a specific value from a list.

items = [10, 20, 30, 40, 50]
items.remove(30)
print("After remove(30):", items)


# 27. Use pop() without index to remove the last item and print the updated list.

last_item = items.pop()
print("Popped last item:", last_item)
print("After pop():", items)



# 28. Use pop(index) to remove the 2nd element in a list.
second_item = items.pop(1)
print("Removed 2nd element (index 1):", second_item)
print("After pop(1):", items)

# 29. Use del to remove an element at index 3.

items = [10, 20, 30, 40, 50]
del items[3]
print("After del at index 3:", items)



# 30. Use clear() to delete all elements and print the empty list.
items.clear()
print("After clear():", items)


# Looping Through Lists (Tasks 31–35)

# 31. Iterate through a list and print all elements in uppercase.

words = ["apple", "banana", "cherry"]
print("Uppercase Words:")
for word in words:
    print(word.upper())


# 32. Write a program to find and print all odd numbers in a list.

numbers = [10, 15, 22, 33, 42, 55]
print("Odd Numbers:")
for num in numbers:
    if num % 2 != 0:
        print(num)


# 33. Print the square of each number in a list using a loop.

numbers1 = [10, 15, 22, 33, 42, 55]
print("Square of Each Numbers:")
for number in numbers1:
      print(f"{number}² = {number ** 2}")


# 34. Use enumerate() to print the index and value of each item.

print("Index and Values:")
for index, value in enumerate(words):
    print(f"Index {index}: {value}")


# 35. Count how many times the word "apple" appears in a list using a loop.

fruits = ["apple", "banana", "apple", "cherry", "apple"]
count = 0
for fruit in fruits:
    if fruit == "apple":
        count += 1
print(f"\n'apple' appears {count} times.")


# ✅ Nested Lists (Tasks 36–40)

# 36. Create a nested list for students with name and marks (e.g., ["John", 85]).

students = [
    ["John", 85],
    ["Emma", 90],
    ["Liam", 78]
]

# 37: Print the name of the 2nd student
print("\nSecond Student's Name:", students[1][0])  # Emma

# 38. Update the marks of the first student in a nested list.

students[0][1] = 95
print("Updated John's Marks:", students[0][1])



# 39. Iterate over a nested list and print all names and marks neatly.

print("\nStudent List:")
for student in students:
    print(f"Name: {student[0]}, Marks: {student[1]}")



# 40. Add a new student to the nested list using append().

students.append(["Olivia", 88])
print("\nUpdated Student List After Adding New Student:")
for student in students:
    print(f"Name: {student[0]}, Marks: {student[1]}")


# Concatenation, Repetition, Slicing (Tasks 41–45)

# 41. Concatenate two lists of numbers and print the result.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated List:", combined)



# 42. Repeat a list of strings 3 times using *.

colors = ["red", "blue"]
repeated = colors * 3
print("Repeated List:", repeated)



# 43. Slice a list to get the first 3 elements.

fruits = ["apple", "banana", "cherry", "date", "strawberry"]
first_three = fruits[:3]
print("First 3 Fruits:", first_three)


# 44. Slice a list to get all elements except the first and last.

middle_fruits = fruits[1:-1]
print("Middle Fruits:", middle_fruits)


# 45. Merge a list of numbers with a list of strings and display the final list.

numbers = [1, 2, 3]
words = ["one", "two", "three"]
merged = numbers + words
print("Merged List:", merged)


# ✅ Membership & Conditional Checks (Tasks 46–50)

# 46. Ask the user for a fruit name and check if it exists in the list using in.

fruit_list = ["apple", "banana", "cherry"]
user_fruit = input("\nEnter a fruit name to check: ").lower()
if user_fruit in fruit_list:
    print(f"{user_fruit} is in the list.")
else:
    print(f"{user_fruit} is NOT in the list.")


# 47. Remove an element only if it exists in the list.

to_remove = "banana"
if to_remove in fruit_list:
    fruit_list.remove(to_remove)
    print(f"{to_remove} removed. Updated list:", fruit_list)
else:
    print(f"{to_remove} not found. List unchanged.")


# 48. Write a program that counts how many times a specific element appears.

animals = ["cat", "dog", "cat", "rabbit", "cat"]
target = "cat"
count = 0
for animal in animals:
    if animal == target:
        count += 1
print(f"\n'{target}' appears {count} times.")



# 49. Check if a number entered by the user exists in a list of marks.

marks = [45, 78, 88, 92, 67]
user_mark = int(input("\nEnter a mark to search: "))
if user_mark in marks:
    print(f"{user_mark} exists in the list.")
else:
    print(f"{user_mark} does not exist in the list.")



# 50. Ask the user for an item and print whether it is present or not in the list.

items = ["pen", "pencil", "notebook", "eraser"]
search_item = input("\nEnter an item to search: ").lower()
if search_item in items:
    print(f"{search_item} is present.")
else:
    print(f"{search_item} is not present.")