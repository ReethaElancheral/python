from attendance_ops import get_attendance_by_student, get_attendance_by_date, get_absentees, get_all_students

def report_by_date(date_str):
    present = get_attendance_by_date(date_str)
    print(f"\n📅 Attendance on {date_str}:")
    for roll, name in get_all_students():
        status = "✅ Present" if roll in present else "❌ Absent"
        print(f"{roll}: {name} - {status}")

def report_by_student(roll_no):
    dates = get_attendance_by_student(roll_no)
    name = next((n for r, n in get_all_students() if r == roll_no), "Unknown")
    print(f"\n📋 {name}'s Attendance:")
    if dates:
        for d in dates:
            print(f"✔️  {d}")
    else:
        print("No attendance found.")

def report_absentees(date_str):
    absentees = get_absentees(date_str)
    print(f"\n🚫 Absentees on {date_str}:")
    for roll, name in get_all_students():
        if roll in absentees:
            print(f"{roll}: {name}")
