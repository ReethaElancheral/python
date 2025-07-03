# 9. User Age Classification System

# Objective: Classify age group.
# Requirements:
# Input: name, age.
# Use if-elif-else:
# <13: Child
# 13–19: Teenager
# 20–59: Adult
# 60+: Senior
# Use comparison and logical operators.


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 13:
    category = "Child"
elif age >=13 and age <= 19:
    category = "Teenager"
elif age>=20 and age<= 59:
    category = "Adult"
else:
    category = "Senior"

print(f"\n{name}, you are classified as: {category}")
