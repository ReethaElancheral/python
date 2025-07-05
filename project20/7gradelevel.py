# ✅ 7. Grade Level Checker

# Objective: Classify student based on marks.
# Requirements:
# Input: total marks.
# Use if-elif-else:
# 90: Excellent, 75–90: Good, 50–75: Average, else: Poor.
# Use variable, float, condition.

marks = float(input("Enter total marks: "))

if marks == 90:
    grade = "Excellent"
elif 75 <= marks < 90:
    grade = "Good"
elif 50 <= marks < 75:
    grade = "Average"
else:
    grade = "Poor"

print(f"Marks: {marks}")
print(f"Grade: {grade}")
