# ✅ 13. Employee Bonus Report Generator

# Objective: Generate bonus report for employees based on performance.
# Requirements:
# Use a list of employees and their scores.
# If score ≥ 90: Excellent → ₹10,000
# If 75–89: Good → ₹5,000
# Else: ₹2,000
# Use for, if-elif-else, and f-string.


employees = [
    ("Nisha", 92),
    ("Reetha", 85),
    ("Mannavan", 70),
    ("Karthi", 90),
    ("Geetha", 76),
    ("Yazh", 60)
]

print("Bonus Report:\n")


for name, score in employees:
    if score >= 90:
        bonus = 10000
        rating = "Excellent"
    elif score >= 75 and score <= 89:
        bonus = 5000
        rating = "Good"
    else:
        bonus = 2000
        rating = "Needs Improvement"

    print(f"{name}: Score = {score}, Rating = {rating}, Bonus = ₹{bonus}")
