# 1. Student Score Tracker

# Goal: Maintain and display student names with their subject scores using tuples.
# Requirements:
# Use a tuple to store each student’s data: (name, (math, physics, chemistry))
# Access subject-wise scores using indexing.
# Find average marks per student using sum() and len().
# Unpack each tuple to display name and subjects separately.
# Prevent accidental modification using tuple immutability.


students = [
    ("Nisha",   (85, 90, 78)),
    ("Reetha",     (70, 88, 92)),
    ("Mannavan",    (95, 60, 80)),
    ("Yazh",   (88, 72, 64)),
    ("Aadhini", (78, 82, 89))
]

def print_scores_and_averages(students_tuple):
    print("\n🧮 Student Scores & Averages")
    print("-------------------------------")
    for name, scores in students_tuple:
        math, phys, chem = scores
        avg = sum(scores) / len(scores)
        print(f"{name}: Math={math}, Physics={phys}, Chemistry={chem} → Average={avg:.2f}")
    print("-------------------------------\n")

print_scores_and_averages(students)

# Demonstrate immutability (uncomment to test)
# students[0][1][0] = 100  # Will raise TypeError
