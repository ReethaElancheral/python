# ✅ 6. Attendance Report Generator

# Objective: Generate attendance for a list of students using enumerate().
# Requirements:
# Input: list of names.
# Output: numbered list with status "Present".
# Use for loop + enumerate() with start=101.

names_input = input("Enter student names separated by commas: ")
students = [name.strip() for name in names_input.split(",")]

print("\nAttendance Report:")
for roll_no, student in enumerate(students, start=101):
    print(f"Roll No. {roll_no}: {student} - Present")
