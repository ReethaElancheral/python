# ✅ 4. Student Score Analyzer

# Objective: Take 5 student marks and find highest, lowest, and average using a loop.
# Requirements:
# Use a for loop to collect 5 marks.
# Store in a list.
# Calculate:
# Max using loop
# Min using loop
# Sum using loop → average
# Use if-else logic to compare.


marks = []

for i in range(5):
    score = float(input(f"Enter mark {i+1}: "))
    marks.append(score)

max_mark = marks[0]
min_mark = marks[0]
total = 0

for mark in marks:

    if mark > max_mark:
        max_mark = mark

    if mark < min_mark:
        min_mark = mark
   
    total += mark

average = total / len(marks)

print(f"Highest mark: {max_mark}")
print(f"Lowest mark: {min_mark}")
print(f"Average mark: {average:.2f}")
