# ✅ 20. Student Attendance System

# Objective: Track student presence.
# Requirements:
# Input: list of student names.
# Input: attendance status ("P" or "A") for each.
# Use for loop to count how many are present. 

students_input = input("Enter student names separated by commas: ").split(',')

students = [name.strip() for name in students_input]

attendance = {}

for student in students:
    status = input(f"Enter attendance for {student} (P/A): ").strip().upper()
    while status not in ['P', 'A']:
        print("Invalid input! Enter 'P' for Present or 'A' for Absent.")
        status = input(f"Enter attendance for {student} (P/A): ").strip().upper()
    attendance[student] = status

present_count = sum(1 for status in attendance.values() if status == 'P')

print(f"\nTotal students present: {present_count} out of {len(students)}")
