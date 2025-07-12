# 15. Class Attendance System

# Description: Maintain daily attendance.
# Store present student names.
# Count absentees by comparing with master list.
# Remove duplicates.

master_list = ["Reetha", "Geetha", "Nisha", "Karthi", "Mannavan"]


present_students = []

def mark_attendance():
    print("Enter present students' names (type 'done' to finish):")
    while True:
        name = input("Student name: ").strip()
        if name.lower() == "done":
            break
        if name in master_list:
            present_students.append(name)
        else:
            print(f"{name} is not in the master list.")

def show_present_students():
    unique_present = list(set(present_students))
    if not unique_present:
        print("No students marked present yet.")
    else:
        print("\nPresent Students (duplicates removed):")
        for student in unique_present:
            print(student)

def count_absentees():
    unique_present = set(present_students)
    absentees = [student for student in master_list if student not in unique_present]
    print(f"\nTotal students: {len(master_list)}")
    print(f"Present students (unique): {len(unique_present)}")
    print(f"Absent students: {len(absentees)}")
    if absentees:
        print("Absent students are:")
        for a in absentees:
            print(a)


while True:
    print("\n--- Class Attendance System ---")
    print("1. Mark Attendance")
    print("2. Show Present Students")
    print("3. Show Absentees Count")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        show_present_students()
    elif choice == "3":
        count_absentees()
    elif choice == "4":
        print("Exiting Attendance System. Bye!")
        break
    else:
        print("Invalid choice.")
