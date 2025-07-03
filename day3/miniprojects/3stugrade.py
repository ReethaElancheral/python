# 🔥 3. Student Grade Evaluator

# Objective: Display grade based on marks.
# Requirements:
# Input: name, marks in 5 subjects.
# Use arithmetic to find average.
# Use if-elif-else:
# ≥90: A
# ≥80: B
# ≥70: C
# else: D
# Use comparison, logical operators, and f-string.

name = input("Enter student name: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

print(f"\nStudent: {name}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
