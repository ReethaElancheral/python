# 🔹 🧮 Arithmetic Operators Tasks (1–8)

# Task 1: Take two numbers as input and print their addition, subtraction, multiplication, and division.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1- num2)
print("Multiplication:", num1* num2)
print("Division:", num1 / num2)


# Task 2: Perform floor division and modulus of two numbers and display with f-string.

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print(f"Floor Division: {first} // {second} = {first // second}")
print(f"Modulus: {first} % {second} = {first % second }")

# Task 3: Use exponentiation ** to calculate power of a number.

base = int(input("Enter base number: "))
power = int(input("Enter power: "))

result = base ** power
print(f"{base} raised to the power {power} is {result}")


# Task 4: Create a calculator that takes 2 inputs and prints all arithmetic results (+, -, *, /, //, %, **)

arith1 = float(input("Enter first number: "))
arith2 = float(input("Enter second number: "))

print(f"Addition: {arith1 + arith2}")
print(f"Subtraction: {arith1 - arith2}")
print(f"Multiplication: {arith1 * arith2}")
print(f"Division: {arith1 / arith2}")
print(f"Floor Division: {arith1 // arith2}")
print(f"Modulus: {arith1 % arith2}")
print(f"Power: {arith1 ** arith2}")

# Task 5: Create a shopping app that adds the prices of 3 items.

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

total = item1 + item2 + item3
print(f"Total bill is: {total}")


# Task 6: Ask user for marks in 5 subjects and calculate average using arithmetic operators.

m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
m5 = float(input("Enter marks for subject 5: "))

average = (m1 + m2 + m3 + m4 + m5) / 5
print(f"Average Marks: {average}")

# Task 7: Convert Celsius to Fahrenheit using arithmetic formula.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")


# Task 8: Use print(f"") to show result of each arithmetic operation with two variables.

arith3 = 12
arith4 = 4

print(f"{arith3} + {arith4} = {arith3 + arith4}")
print(f"{arith3} - {arith4} = {arith3 - arith4}")
print(f"{arith3} * {arith4} = {arith3 * arith4}")
print(f"{arith3} / {arith4} = {arith3 / arith4}")
print(f"{arith3} // {arith4} = {arith3 // arith4}")
print(f"{arith3} % {arith4} = {arith3 % arith4}")
print(f"{arith3} ** {arith4} = {arith3 ** arith4}")


# 🔹 🧮 Comparison Operators Tasks (9–14)

# Task 9: Compare two user-input numbers using all 6 comparison operators and print results.

com1 = float(input("Enter first number: "))
com2 = float(input("Enter second number: "))

print(f"{com1} == {com2} ➝ {com1 == com2}")
print(f"{com1} != {com2} ➝ {com1 != com2}")
print(f"{com1} > {com2} ➝ {com1 > com2}")
print(f"{com1} < {com2} ➝ {com1 < com2}")
print(f"{com1} >= {com2} ➝ {com1 >= com2}")
print(f"{com1} <= {com2} ➝ {com1 <= com2}")

# Task 10: Write a program to check if a person is older than 18.

age = int(input("Enter your age: "))
is_adult = age > 18

print(f"Are you older than 18? ➝ {is_adult}")

# Task 11: Take two strings and check if they are equal or not using ==, !=.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print(f"Strings are equal? ➝ {str1 == str2}")
print(f"Strings are not equal? ➝ {str1 != str2}")

# Task 12: Ask for two exam scores and compare which one is higher using >, <.

score1 = float(input("Enter score of exam 1: "))
score2 = float(input("Enter score of exam 2: "))

print(f"Exam 1 > Exam 2 ➝ {score1 > score2}")
print(f"Exam 1 < Exam 2 ➝ {score1 < score2}")

# Task 13: Use >= and <= to check if the number lies in a particular range.
num = int(input("Enter a number: "))

in_range = num >= 10 and num <= 100
print(f"Is the number between 10 and 100 (inclusive)? ➝ {in_range}")

# Task 14: Create a simple program to check if a user entered score is a passing mark (above 50).

score = int(input("Enter your score: "))

is_pass = score > 50
print(f"Did you pass? ➝ {is_pass}")

# 🔹 🔐 Logical Operators Tasks (15–20)

# Task 15: Use and to check if age is above 18 and the person has an ID.
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

can_enter = age > 18 and has_id
print(f"Can the person enter? ➝ {can_enter}")


# Task 16: Use or to check if a user entered "yes" or "y" as confirmation.
confirm = input("Do you want to continue? (yes/y): ").lower()

is_confirmed = confirm == "yes" or confirm == "y"
print(f"Confirmed? ➝ {is_confirmed}")


# Task 17: Use not to reverse a comparison result.
marks = int(input("Enter your marks: "))

fail = not (marks >= 35)
print(f"Did the student fail? ➝ {fail}")


# Task 18: Create a program to allow club entry only if age ≥ 21 and dress code is “formal”.
age = int(input("Enter your age: "))
dress = input("Enter your dress code (formal/casual): ").lower()

entry_allowed = age >= 21 and dress == "formal"
print(f"Allowed to enter the club? ➝ {entry_allowed}")


# Task 19: Ask user two boolean inputs and evaluate them using all logical operators.
val1 = input("Enter first value (true/false): ").lower() == "true"
val2 = input("Enter second value (true/false): ").lower() == "true"

print(f"{val1} and {val2} ➝ {val1 and val2}")
print(f"{val1} or {val2} ➝ {val1 or val2}")
print(f"not {val1} ➝ {not val1}")


# Task 20: Combine multiple conditions using and/or and print pass/fail logic.
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))

passed = math >= 40 and science >= 40

print(f"Pass Status: {'PASS' if passed else 'FAIL'}")

# 🔹 🖊️ Assignment Operators Tasks (21–26)

# Task 21: Initialize a variable with 10 and use +=, -=, *=, /=, //=, %= to update its value.
oper1 = 10
print("Initial value:", oper1)

oper1 += 5
print("After += 5:", oper1)

oper1 -= 2
print("After -= 2:", oper1)

oper1 *= 3
print("After *= 3:", oper1)

oper1 /= 4
print("After /= 4:", oper1)

oper1 //= 2
print("After //= 2:", oper1)

oper1 %= 3
print("After %= 3:", oper1)


# Task 22: Take a number and increment it by 5 using +=.
num = int(input("Enter a number: "))
num += 5
print(f"Number after adding 5: {num}")


# Task 23: Calculate area of a square and double it using *=.
side = float(input("Enter side of square: "))
area = side * side
print(f"Original Area: {area}")

area *= 2
print(f"Doubled Area: {area}")


# Task 24: Take a salary amount and apply tax deduction using -=.
salary = float(input("Enter your salary: "))
tax = float(input("Enter tax amount to deduct: "))

salary -= tax
print(f"Salary after tax deduction: {salary}")


# Task 25: Build a step-by-step program that modifies a variable using every assignment operator.
oper2 = 20
print("Start value:", oper2)

oper2+= 10
print("After += 10:", oper2)

oper2 -= 5
print("After -= 5:", oper2)

oper2 *= 2
print("After *= 2:", oper2)

oper2 /= 5
print("After /= 5:", oper2)

oper2 //= 2
print("After //= 2:", oper2)

oper2 %= 4
print("After %= 4:", oper2)


# Task 26: Create a mini bank balance simulator using assignment operators to update deposits/withdrawals.

balance = 1000  #
print(f"Initial Balance: {balance}")

deposit = float(input("Enter deposit amount: "))
balance += deposit
print(f"Balance after deposit: {balance}")

withdraw = float(input("Enter withdrawal amount: "))
balance -= withdraw
print(f"Balance after withdrawal: {balance}")

# 🔹 🪪 Identity Operators Tasks (27–30)

# Task 27: Compare two identical lists using is and print if they refer to the same memory.
list1 = [1, 2, 3]
list2 = list1 

print("list1 is list2:", list1 is list2)  


# Task 28: Compare two different but equal lists using is not.
list1 = [1, 2, 3]
list2 = [1, 2, 3] 

print("list1 == list2:", list1 == list2)    
print("list1 is not list2:", list1 is not list2)  


# Task 29: Show that a = b means both a is b is True (same memory) only for non-mutable objects.
a = 100
b = a  

print("a is b:", a is b)  


# Task 30: Create three variables, two referencing the same list and one different, compare using is, is not.

ref1 = [4, 5, 6]
ref2 = ref1   
ref3 = [4, 5, 6]  

print("x is y:", ref1 is ref2)       
print("x is z:", ref1 is ref3)        
print("y is not z:", ref2 is not ref3)  

# 🔹 📜 Membership Operators Tasks (31–35)

# Task 31: Check if a letter is present in a string using in.
text = "python programming"
letter = input("Enter a letter to check: ")

print(f"Is '{letter}' in the string? ➝ {letter in text}")


# Task 32: Ask user for a fruit name and check if it is in your predefined fruit list.
fruits = ["apple", "banana", "orange", "kiwi"]
fruit = input("Enter a fruit name: ").lower()

print(f"Is '{fruit}' in the list? ➝ {fruit in fruits}")


# Task 33: Use not in to check if a number is not in a list.
numbers = [10, 20, 30, 40, 50]
num = int(input("Enter a number: "))

print(f"Is {num} NOT in the list? ➝ {num not in numbers}")


# Task 34: Search for a word in a sentence using in and display if it’s found.
sentence = "Learning Python is fun and useful"
word = input("Enter a word to search: ").lower()

print(f"Is '{word}' found in the sentence? ➝ {word in sentence.lower()}")


# Task 35: Check if a key exists in a dictionary using in.
student = {
    "name": "Reetha",
    "age": 20,
    "grade": "A"
}

key = input("Enter key to check (name, age, grade): ").lower()
print(f"Is '{key}' a key in the dictionary? ➝ {key in student}")


# 🔹 🔧 Bitwise Operators Tasks (36–40)

# Task 36: Take two integers and perform bitwise AND (&), OR (|), XOR (^).
bitwise1 = int(input("Enter first number: "))
bitwise2 = int(input("Enter second number: "))

print(f"{bitwise1} & {bitwise2} = {bitwise1 & bitwise2}")
print(f"{bitwise1} | {bitwise2} = {bitwise1 | bitwise2}")
print(f"{bitwise1} ^ {bitwise2} = {bitwise1 ^ bitwise2}")


# Task 37: Demonstrate NOT (~) on a positive number.
num = int(input("Enter a positive number: "))

result = ~num
print(f"~{num} = {result}")


# Task 38: Perform left shift << and right shift >> on a number and display binary.
num = int(input("Enter a number: "))

left = num << 1
right = num >> 1

print(f"Binary of {num} ➝ {bin(num)}")
print(f"{num} << 1 ➝ {left} (Binary: {bin(left)})")
print(f"{num} >> 1 ➝ {right} (Binary: {bin(right)})")


# Task 39: Show binary representation using bin() and apply bitwise operations.
bin1 = int(input("Enter first number: "))
bin2 = int(input("Enter second number: "))

print(f"Binary of {bin1}: {bin(bin1)}")
print(f"Binary of {bin2}: {bin(bin2)}")
print(f"{bin1} & {bin2} = {bin1 & bin2} ➝ {bin(bin1 & bin2)}")
print(f"{bin1} | {bin2} = {bin1 | bin2} ➝ {bin(bin1 | bin2)}")
print(f"{bin1} ^ {bin2} = {bin1 ^ bin2} ➝ {bin(bin1 ^ bin2)}")


# Task 40: Create a bit mask simulation using bitwise operations for toggling bits.
number = 0b1010  
mask = 0b0101   

result = number ^ mask

print(f"Original : {bin(number)}")
print(f"Mask     : {bin(mask)}")
print(f"Toggled  : {bin(result)}")


# 🔹 🧠 Conditional Statements – Basic (41–45)

# Task 41: Ask user for age and print if eligible to vote using if.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")


# Task 42: Ask for age, print "Minor" if less than 18, else "Adult" using if-else.
age = int(input("Enter your age: "))
if age < 18:
    print("Minor")
else:
    print("Adult")


# Task 43: Ask for marks and print grades using:

# if ≥ 90: A
# elif ≥ 80: B
# elif ≥ 70: C
# else: Fail

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Fail")


# Task 44: Ask for temperature and print:
# "Hot" if above 35
# "Warm" if between 25–35
# "Cool" otherwise

temp = float(input("Enter temperature in °C: "))
if temp > 35:
    print("Hot")
elif temp <= 35 or temp >=25:
    print("Warm")
else:
    print("Cool")




# Task 45: Ask for a number and print if it is even or odd using if-else.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# 🔹 🧠 Conditional Statements – Intermediate (46–50)

# Task 46: Ask for username and password using if-else to simulate login check.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password.")


# Task 47: Ask if it's raining (yes/no), and whether the user has an umbrella. Use nested if.
raining = input("Is it raining? (yes/no): ").lower()
if raining == "yes":
    umbrella = input("Do you have an umbrella? (yes/no): ").lower()
    if umbrella == "yes":
        print("You can go outside.")
    else:
        print("Better stay inside.")
else:
    print("You can go outside.")


# Task 48: Ask user for age and nationality. Allow voting if age ≥ 18 and nationality is "Indian". Use if and and.
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()

if age >= 18 and nationality == "indian":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Task 49: Build a calculator:

# If user chooses "add", perform addition
# If "sub", perform subtraction
# Use if-elif-else

operation = input("Choose operation (add/sub): ").lower()
cal1 = float(input("Enter first number: "))
cal2 = float(input("Enter second number: "))

if operation == "add":
    print("Result:", cal1 + cal2)
elif operation == "sub":
    print("Result:", cal1 - cal2)
else:
    print("Invalid operation.")



# Task 50: Ask for exam result (marks, attendance). If marks ≥ 40 and attendance ≥ 75%, print "Passed", else "Failed".

marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance %: "))

if marks >= 40 and attendance >= 75:
    print("Result: Passed")
else:
    print("Result: Failed")

