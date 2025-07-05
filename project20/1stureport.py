# ✅ 1. Student Report Card Generator

# Objective: Generate a simple report card.
# Requirements:
# Use variables to store student name, class, and marks (list).
# Use a for loop to calculate total and average.
# Use if-elif-else to assign grade:
# ≥90: A, 80–89: B, 70–79: C, else: D.
# Print report using f-string.


name = input("Enter student name: ")
class_name = input("Enter class: ")


marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark {i}: "))
    marks.append(mark)


total = 0
for m in marks:
    total += m

average = total / len(marks)


if average >= 90:
    grade = "A"
elif average >= 80 and average <=89:
    grade = "B"
elif average >= 70 and average <=79:
    grade = "C"
else:
    grade = "D"


print("\n📄 Student Report Card")
print(f"Name     : {name}")
print(f"Class    : {class_name}")
print(f"Marks    : {marks}")
print(f"Total    : {total}")
print(f"Average  : {average:.2f}")
print(f"Grade    : {grade}")
