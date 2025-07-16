# 11. School Attendance Tracker

# Description: Manage student attendance per day.
# Requirements:
# - Structure: {date: [student_names_present]}
# - Add attendance for each day
# - Mark absentees
# - Use .keys() to get all dates
# - Reverse query: for a student, show attendance count


attendance = {
    "2025-07-01": ["Alice", "Bob", "Charlie"],
    "2025-07-02": ["Alice", "David"],
    "2025-07-03": ["Bob", "Charlie", "David"],
}

def mark_attendance(date, present_students):
    """Mark attendance for a specific date."""
    attendance[date] = present_students

def get_all_dates():
    """Retrieve all dates with attendance records."""
    return list(attendance.keys())

def get_student_attendance(student_name):
    """Retrieve the count of days a student was present."""
    return sum(student_name in present for present in attendance.values())

def get_absentees(date, all_students):
    """Retrieve a list of students who were absent on a specific date."""
    present_students = attendance.get(date, [])
    return [student for student in all_students if student not in present_students]


mark_attendance("2025-07-04", ["Alice", "Charlie", "David"])
print("All Dates:", get_all_dates())
print("Alice's Attendance Count:", get_student_attendance("Alice"))
print("Absentees on 2025-07-03:", get_absentees("2025-07-03", ["Alice", "Bob", "Charlie", "David"]))
