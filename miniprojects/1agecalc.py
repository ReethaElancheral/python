## 1. Age Calculator


# - Prompt the user to enter their birth year.
# - Calculate their current age.
# - Display the age using an f-string.
# - Use type() to show the type of the age variable.

birth_year = input("Enter Your Birth year:")
birth_year = int(birth_year)
current_year = 2025
age = current_year - birth_year
print(f" You are {age} years old")
print("The Type of 'age' Variable is:", type(age))
