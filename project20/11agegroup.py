# ✅ 11. Age Group Classifier

# Objective: Classify person based on age.
# Requirements:
# Input: age (int).
# Use if-elif-else:
# <13: Child, 13–19: Teen, 20–59: Adult, 60+: Senior

age = int(input("Enter age: "))

if age < 13:
    group = "Child"
elif 13 <= age <= 19:
    group = "Teen"
elif 20 <= age <= 59:
    group = "Adult"
else:
    group = "Senior"

print(f"Age: {age} → Group: {group}")
