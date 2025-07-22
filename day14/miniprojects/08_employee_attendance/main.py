from attendance.register import mark_attendance
from attendance.report import generate_report

def main():
    while True:
        print("\n=== Employee Attendance Register ===")
        print("1. Mark Attendance")
        print("2. Generate Attendance Report")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            name = input("Enter employee name: ").strip()
            mark_attendance(name)
        elif choice == '2':
            name = input("Enter employee name for report: ").strip()
            generate_report(name)
        elif choice == '3':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
