from attendance_ops import mark_attendance, get_all_students
from report_utils import report_by_date, report_by_student, report_absentees

def main():
    while True:
        print("\n--- Attendance System ---")
        print("1. Mark Attendance")
        print("2. View by Date")
        print("3. View by Student")
        print("4. View Absentees by Date")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_str = input("Enter date (YYYY-MM-DD): ")
            print("Students:")
            for roll, name in get_all_students():
                print(f"{roll}: {name}")
            present_input = input("Enter roll numbers of present students (comma separated): ")
            present_rolls = [int(r.strip()) for r in present_input.split(",") if r.strip().isdigit()]
            mark_attendance(date_str, present_rolls)
            print("Attendance marked.")

        elif choice == "2":
            date_str = input("Enter date (YYYY-MM-DD): ")
            report_by_date(date_str)

        elif choice == "3":
            roll_no = int(input("Enter roll number: "))
            report_by_student(roll_no)

        elif choice == "4":
            date_str = input("Enter date (YYYY-MM-DD): ")
            report_absentees(date_str)

        elif choice == "0":
            print("Exiting Attendance System.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
