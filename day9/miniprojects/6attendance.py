# 6. Classroom Attendance Register

# Goal: Record daily student attendance using tuples.
# Requirements:
# Store attendance as (date, (student1, student2, ...))
# Use nested tuples for student grouping.
# Access a specific day's attendance using slicing.
# Count how many days a student was present using .count().
# Use tuple unpacking to get date and students.


attendance = [
    ("2025-07-10", ("Alice", "Bob", "Charlie")),
    ("2025-07-11", ("Alice", "David")),
    ("2025-07-12", ("Bob", "Elaine", "Frank")),
    ("2025-07-13", ("Alice", "Charlie", "Frank")),
    ("2025-07-14", ("Bob", "Charlie", "Elaine")),
    ("2025-07-15", ("Alice", "Bob")),
    ("2025-07-16", ("Charlie", "David", "Frank"))
]


def show_attendance(records):
    print("\n📅 Attendance Records")
    print("----------------------")
    for date, students in records:
      
        print(f"{date}: {', '.join(students)}")
    print("----------------------\n")


show_attendance(attendance)


last_three = attendance[-3:] 
print("🔍 Last 3 days attendance:")
show_attendance(last_three)


def days_present(student, records):
   
    return sum(1 for _, students in records if students.count(student) > 0)

print("✅ Attendance Count:")
for name in ("Alice", "Bob", "Charlie"):
    print(f"{name}: {days_present(name, attendance)} days")


day_index = 2 
date, students = attendance[day_index] 
print(f"\n📌 Attendance on {date}: {', '.join(students)}")
