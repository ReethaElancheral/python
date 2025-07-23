# 15. Student Attendance Tracker

# Use Case: Accept attendance entries per student. 
# Exception Handling Goals:
# Raise error if attendance > max days
# Catch invalid roll numbers
# Log absentees with exception info
# Use loop with try-except for multiple students

import logging

# Setup logging
logging.basicConfig(filename="absentees.log", level=logging.INFO, format='%(asctime)s - %(message)s')

MAX_DAYS = 30

class AttendanceError(Exception):
    pass

def student_attendance_tracker():
    num_students = 0
    try:
        num_students = int(input("Enter number of students: "))
    except ValueError:
        print("❌ Invalid number entered. Exiting.")
        return

    for _ in range(num_students):
        try:
            roll = input("\nEnter student roll number (numeric): ")
            if not roll.isdigit():
                raise ValueError("Roll number must be numeric.")

            attendance = int(input(f"Enter attendance days for roll {roll} (max {MAX_DAYS}): "))
            if attendance > MAX_DAYS or attendance < 0:
                raise AttendanceError(f"Attendance {attendance} out of valid range 0-{MAX_DAYS}.")

            if attendance < (MAX_DAYS // 2):
                logging.info(f"Roll {roll} absenteeism detected: attendance={attendance}")
                print(f"⚠️ Student roll {roll} has low attendance.")

            else:
                print(f"✅ Attendance recorded for roll {roll}: {attendance} days.")

        except ValueError as ve:
            print(f"❌ Invalid input: {ve}. Skipping student.")
        except AttendanceError as ae:
            print(f"❌ Attendance error: {ae}. Skipping student.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}. Skipping student.")

    print("\n📝 Attendance processing complete.")

if __name__ == "__main__":
    student_attendance_tracker()
