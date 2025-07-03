## 1. Setup, Introduction, and print()

#1. Print "Hello, Python!" to the output.
print("Hello, Python!")

# 2. Print your name and age using a single print() statement.

Name = "Reetha"
Age = 33
print("Name:", Name, ","  "age:", Age)

# 3. Use print() to display three favorite fruits, separated by commas (using sep).

print("Kiwi", "Pomegranate", "Strawberry", sep=",")

# 4. Print "Python is fun" three times, all on the same line, using the end parameter.

print("Python is fun", end=" ")
print("Python is fun", end=" ")
print("Python is fun")

# 5. Use print() and f-strings to display: My favorite number is 42.

favorite_number = 42
print(f"My favorite number is {favorite_number}.")

# 6. Print the result of 5 + 7 using print().
print(5 + 7)

# 7. Write a comment in Python explaining what the print() function does.
# The print() function displays the specified message or value to the screen.

# 8. Combine print() with variables to display a message.
name = "Reetha"
language = "Python"
print(name + " is learning " + language + ".")

# 9. Use print() to show the output: Apple | Banana | Cherry (use sep).
print("Apple", "Banana", "Cherry", sep=" | ")

# 10. Print your city and country, each on a separate line, in a single print() call.
print("Doha\nQatar")

## 2. Variables and Data Types

# 11. Create a variable called name and assign your first name. Print it.
name = "Reetha"
print(name)

# 12. Create a variable age and assign your age. Print it.
age = 25
print(age)

# 13. Create a float variable price, assign a value, and print it.
price = 49.99
print(price)

# 14. Define a boolean variable is_student and print its value.
is_student = True
print(is_student)

# 15. Make a list of three favorite colors and print the second color.
colors = ["Red", "Blue", "Green"]
print(colors[1])

# 16. Create a tuple called coordinates with two numbers and print both values.
coordinates = (10.5, 20.8)
print(coordinates[0], coordinates[1])

# 17. Define a dictionary with keys "brand" and "year" for a car. Print both values.
car = {"brand": "Toyota", "year": 2022}
print(car["brand"], car["year"])

# 18. Create a set of three unique numbers and print the set.
unique_numbers = {1, 2, 3}
print(unique_numbers)

# 19. Change the value of a variable after assigning it. Print before and after.
language = "Python"
print("Before:", language)
language = "JavaScript"
print("After:", language)

# 20. Assign a string to a variable, then print its type using type().
city = "Doha"
print(type(city))

## 3. Data Types: Examples

# 21. Assign an integer to a variable and print it.
my_int = 100
print(my_int)

# 22. Assign a float to a variable and print it.
my_float = 3.14
print(my_float)

# 23. Assign a string with your favorite quote and print it.
quote = "The only way to do great work is to love what you do."
print(quote)

# 24. Assign True to a boolean variable and print it.
is_active = True
print(is_active)

# 25. Create a list of five subjects and print the last subject.
subjects = ["Math", "Science", "English", "History", "Computer"]
print(subjects[-1])

# 26. Make a tuple of three city names and print the first one.
cities = ("Doha", "London", "Tokyo")
print(cities[0])

# 27. Store information about a student (name, grade) in a dictionary and print it.
student = {"name": "Reetha", "grade": "A"}
print(student["name"], student["grade"])

# 28. Add duplicate values to a set and print the set.
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # Duplicates are automatically removed in a set

# 29. Store different data types in a list and print each with its type using a loop.
mixed_list = [123, 3.14, "Hello", True]
for item in mixed_list:
    print(item, type(item))

# 30. Use a variable to store a value, then use type() to print its data type.
data = "Python is powerful"
print(type(data))


## 4. input() and f-strings

# 31. Ask the user for their name using input(), then greet them.
name = input("What is your name? ")
print("Hello,", name + "!")

# 32. Ask for two numbers (as input), add them, and print the result.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The sum is:", num1 + num2)

# 33. Use input() to get a user's age, then print how old they'll be next year.
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

# 34. Ask the user for their favorite color and print a message using f-string.
color = input("What is your favorite color? ")
print(f"Wow! {color} is a beautiful color!")

# 35. Get the user's city and country with input(), then print a formatted message.
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"You live in {city}, {country}.")

# 36. Ask for a price and a discount, calculate the discounted price, and print it using f-string.
price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))
discounted_price = price - (price * discount / 100)
print(f"The discounted price is: {discounted_price}")

# 37. Use input() to get three hobbies, store them in a list, and print the list.
hobby1 = input("Enter your first hobby: ")
hobby2 = input("Enter your second hobby: ")
hobby3 = input("Enter your third hobby: ")
hobbies = [hobby1, hobby2, hobby3]
print("Your hobbies are:", hobbies)

# 38. Ask the user for their name and age, then print: "Alice is 25 years old." (replace with inputs)
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"{name} is {age} years old.")

# 39. Write a program that asks for two numbers, multiplies them, and prints the answer with f-string.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 * num2
print(f"The result of multiplication is: {result}")

# 40. Use input() to get a string, then print its type using type().
user_input = input("Enter something: ")
print("Type of input is:", type(user_input))

## 5. type() Function and Data Type Checks


# 41. Create a variable with a value, then print its type using type().
value = 123
print(type(value))

# 42. Use type() to check the type of user input.
user_input = input("Enter something: ")
print("The type of your input is:", type(user_input))

# 43. Store a number as string using input(), then convert it to int and print both types.
num_str = input("Enter a number: ")
num_int = int(num_str)
print("Before conversion:", type(num_str))
print("After conversion:", type(num_int))

# 44. Make a list with different data types and print each value with its type (using a loop).
mixed = [10, "text", 3.14, False]
for item in mixed:
    print(item, "is of type", type(item))

# 45. Use type() to confirm that True is of type bool.
print(type(True)) 

# 46. Ask the user for their birth year, convert it to int, and print its type.
birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)
print("Type of birth year:", type(birth_year))

# 47. Create a tuple and print the type of the tuple.
my_tuple = (1, 2, 3)
print("Type of my_tuple:", type(my_tuple))

# 48. Make a set, then print the set and its type.
my_set = {10, 20, 30}
print("Set:", my_set)
print("Type of my_set:", type(my_set))

# 49. Use type() to determine the data type of a value inside a dictionary.
person = {"name": "Alice", "age": 30}
print("Type of 'age' value:", type(person["age"]))

# 50. Write a program that asks for a number, prints its type, then prints its type after converting to float.
num = input("Enter a number: ")
print("Before conversion:", type(num))
num = float(num)
print("After conversion:", type(num))


