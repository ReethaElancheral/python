# ✅ 12. Marks to Grade Converter

# Objective: Convert a mark list to grades.
# Requirements:
# Input list of marks.
# Use for loop with if-elif-else inside loop to print grades.

marks_input = input("Enter marks separated by commas: ").split(',')

marks = [int(mark.strip()) for mark in marks_input]

print("\nGrades:")
for mark in marks:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"Mark: {mark} → Grade: {grade}")
