# ✅ 1. Student Roll Call System

# Objective: Take attendance for a classroom.
# Requirements:
# Use a while loop to enter student names one by one.
# Stop after a total of 10 students are entered.
# Skip empty names using continue.
# Use else after loop to print “Attendance completed!”

students = []
count = 0

while count < 10:
    name = input(f"Enter name for student {count + 1}: ").strip()

    if name == "":
        print("Empty name skipped.")
        continue  

    students.append(name)
    count += 1
else:
    print("\nAttendance completed!")
    print("Student List:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")
