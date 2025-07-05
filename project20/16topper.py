# ✅ 16. Topper Finder in Class


# Objective: Find student with highest marks.
# Requirements:
# Use dictionary: student → marks.
# Use loop to find max.
# Print topper name and mark.

students = {
    "Reetha": 88,
    "Nisha": 92,
    "Geetha": 85,
    "Mannavan": 95,
    "Karthiga": 90
}

topper_name = None
topper_marks = -1

for student, marks in students.items():
    if marks > topper_marks:
        topper_marks = marks
        topper_name = student

print(f"Topper: {topper_name} with marks {topper_marks}")
