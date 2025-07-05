# ✅ 🔁 Basic For Loop Tasks (1–10)

# Task 1: Print all elements in the list ["Pen", "Pencil", "Eraser"] using a for loop.
list_items = ["Pen", "Pencil", "Eraser"];
for listed in list_items:
    print(listed)

# Task 2: Print each character in the string "Vetri" one by one.
name = "Vetri"
for char in name:
    print(char)

# Task 3: Use range() to print numbers from 1 to 10.
for num in range(1,11):
    print(num)


# Task 4: Print all odd numbers from 1 to 20 using range() with step.
for odd_num in range(1,21,2):
    print(odd_num)

# Task 5: Create a list of 5 colors and print them using a for loop.
colors = ["Red", "Blue", "Green", "Yellow", "Pink"]
for color in colors:
    print(color)


# Task 6: Use range() to print numbers from 10 to 1 (reverse order).
for num1 in range(10, 0, -1):
    print(num1)


# Task 7: Ask user to enter a number n, and print numbers from 1 to n.
n = int(input("Enter a number: "))
for num2 in range(1, n + 1):
    print(num2)


# Task 8: Create a list of fruits, use a loop to print “I like <fruit>” for each fruit.
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
for fruit in fruits:
    print(f"I like {fruit}")


# Task 9: Print the multiplication table of 5 using a loop.
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# Task 10: Calculate the sum of numbers from 1 to 50 using a for loop.

total = 0
for num in range(1, 51):
    total += num
print(f"Sum of numbers from 1 to 50 is: {total}")

# ✅ 🔠 For Loop with Strings (11–15)

# Task 11: Print all vowels in "Technology" using a for loop.
text = "Technology"
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        print(char)


# Task 12: Count and display the number of vowels in a given string.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")


# Task 13: Count the number of lowercase letters in "Python Loop Practice".
text = "Python Loop Practice"
count = 0

for char in text:
    if char.islower():
        count += 1

print(f"Number of lowercase letters: {count}")


# Task 14: Print each word in the string "Learn Python Fast" using .split() and loop.
sentence = "Learn Python Fast"
words = sentence.split()

for word in words:
    print(word)


# Task 15: Reverse a string using a for loop (without using slicing).
original = "Python"
reversed_string = ""

for char in original:
    reversed_string = char + reversed_string 

print(f"Reversed string: {reversed_string}")

# ✅ 🔢 Range() with For Loop (16–20)

# Task 16: Print all numbers between 1 and 50 that are divisible by 5.
for num in range(1, 51):
    if num % 5 == 0:
        print(num)


# Task 17: Print even numbers between 2 and 20 using range(start, stop, step).
for num in range(2, 21, 2):
    print(num)


# Task 18: Ask for a starting and ending number from the user and print the range.
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    print(num)


# Task 19: Create a loop that prints powers of 2 (2, 4, 8, 16, ...) up to 1024.
for exponent in range(1, 11):  
    print(2 ** exponent)



# Task 20: Print the square of each number from 1 to 10 using a for loop.
for num in range(1, 11):
    print(f"{num}² = {num ** 2}")


# ✅ 🔂 Control Statements – break, continue, pass, else (21–30)

# Task 21: Loop from 1 to 10 and break the loop if number is 5.
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# Task 22: Loop from 1 to 10 and continue (skip) if the number is 5.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Task 23: Use pass in a loop where you want to add code later.
for i in range(1, 6):
    pass 


# Task 24: Ask the user to enter 5 numbers, break if a number is negative.
for i in range(5):
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered, breaking loop.")
        break


# Task 25: Use continue to skip even numbers and print only odd numbers from 1 to 10.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# Task 26: Print numbers from 1 to 3, and print “Loop complete!” using else with loop.
for i in range(1, 4):
    print(i)
else:
    print("Loop complete!")

# Task 27: Print all elements in a list, but stop the loop if the item is "Stop".
items = ["Apple", "Banana", "Stop", "Orange"]
for item in items:
    if item == "Stop":
        break
    print(item)


# Task 28: Loop through "VetriTech" and skip the letter "T" using continue.
for char in "VetriTech":
    if char == "T" or char == "t":
        continue
    print(char)


# Task 29: Loop through 1 to 10. Use pass when number is divisible by 3.
for i in range(1, 11):
    if i % 3 == 0:
        pass  
    else:
        print(i)


# Task 30: Demonstrate a for loop that runs else when loop completes without break.
for i in range(1, 6):
    print(i)
else:
    print("Loop completed without break.")


# ✅ 🔁 enumerate() Function (31–35)

# Task 31: Use enumerate() to print index and value for "Python".
for index, char in enumerate("Python"):
    print(f"Index {index}: {char}")

# Task 32: Use enumerate() with a fruit list to print like:
# markdownCopyEdit1. Apple  2. Banana  3. Cherry
fruits = ["Apple", "Banana", "Cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}", end="  ")


# Task 33: Use enumerate() to display character positions in "Hello World".
text = "Hello World"
for position, letter in enumerate(text):
    print(f"Character '{letter}' at position {position}")


# Task 34: Create a list of students and print roll number using enumerate(start=101).
students = ["Aisha", "Ravi", "Priya", "Manoj"]
for roll_no, name in enumerate(students, start=101):
    print(f"Roll No. {roll_no}: {name}")


# Task 35: Use enumerate() inside a function that labels each item in a menu list.
menu = ["Home", "About", "Services", "Contact"]

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")

# ✅ 🔁 Nested For Loops (36–45)

# Task 36: Create a multiplication table for numbers 1 to 3 using nested loops.
for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("----------")


# Task 37: Use nested loop to print this pattern:
# markdownCopyEdit* * ** * ** * * *
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()



# Task 38: Print a number triangle:
# CopyEdit1  
# 1 2  
# 1 2 3  
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Task 39: Create a nested loop that prints all pair combinations from two lists.
list1 = [1, 2]
list2 = ['A', 'B']

for i in list1:
    for j in list2:
        print((i, j))


# Task 40: Create a multiplication chart from 1x1 to 5x5.
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j}", end="\t")
    print()


# Task 41: Print a right-angled triangle using nested loops with alphabets:
# cssCopyEditAB B  
# C C C
ch = 65  # ASCII for 'A'
for i in range(1, 4):
    for j in range(i):
        print(chr(ch), end=" ")
    ch += 1
    print()


# Task 42: Ask for user input and print a triangle pattern with their name characters.
name = input("Enter your name: ")

for i in range(1, len(name)+1):
    for j in range(i):
        print(name[j], end=" ")
    print()

# Task 43: Create a pattern like:
# CopyEdit1  
# 2 2  
# 3 3 3  
# 4 4 4 4
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()


# Task 44: Print a grid of size 3x3 using nested loops:
# shellCopyEdit# # # # # # # # # 
for i in range(3):
    for j in range(3):
        print("#", end=" ")
    print()


# Task 45: Create a star pattern using nested loop with custom rows and columns.
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()


# ✅ 🧠 Logic-Based Loop Tasks (46–50)


# Task 46: Write a program to print the factorial of a number using a loop.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")


# Task 47: Ask for 5 numbers, store them in a list, and print the maximum using loop.
nums = []
for _ in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)

maximum = nums[0]
for n in nums:
    if n > maximum:
        maximum = n

print(f"Maximum number: {maximum}")


# Task 48: Reverse a list manually using a for loop.
original = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(original)-1, -1, -1):
    reversed_list.append(original[i])

print("Reversed list:", reversed_list)


# Task 49: Print the Fibonacci series up to n terms using a for loop.
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Task 50: Create a program that finds all prime numbers from 1 to 50 using nested loops.
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
