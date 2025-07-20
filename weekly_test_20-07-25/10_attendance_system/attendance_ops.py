from datetime import datetime
from attendance_data import students, attendance_record

def mark_attendance(date_str, present_rolls):
    attendance_record[date_str] = set(present_rolls)

def get_attendance_by_date(date_str):
    return attendance_record.get(date_str, set())

def get_attendance_by_student(roll_no):
    present_dates = [date for date, present in attendance_record.items() if roll_no in present]
    return present_dates

def get_all_students():
    return students

def get_absentees(date_str):
    present = get_attendance_by_date(date_str)
    all_rolls = {roll for roll, _ in students}
    return all_rolls - present
