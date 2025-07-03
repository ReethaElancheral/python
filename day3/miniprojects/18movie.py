# 18. Movie Ticket Price Calculator

# Objective: Calculate ticket price based on age group.
# Requirements:
# Use:
# Child < 12: ₹50
# Adult 12–60: ₹120
# Senior > 60: ₹100
# Use if-elif-else.


age = int(input("Enter your age: "))
if age < 12:
    price = 50
elif 12 <= age <= 60:
    price = 120
else:  
    price = 100

print(f"Ticket price for age {age} is: ₹{price}")
