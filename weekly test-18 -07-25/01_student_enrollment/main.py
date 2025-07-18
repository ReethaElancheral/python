from student_utils.enrollment import add_student, enroll_course
from student_utils.courses import get_available_courses

def main():
    students = {}
    available_courses = get_available_courses()

    while True:
        print("\n--- Student Course Enrollment ---")
        print("1. Add Student")
        print("2. Enroll in Course")
        print("3. View Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            student_id = (sid,)  # tuple ID
            add_student(students, student_id, name)

        elif choice == "2":
            sid = input("Enter Student ID: ")
            student_id = (sid,)
            if student_id not in students:
                print("Student not found.")
                continue
            print("Available Courses:", ", ".join(available_courses))
            course = input("Enter Course to Enroll: ")
            enroll_course(students, student_id, course, available_courses)

        elif choice == "3":
            for sid, data in students.items():
                print(f"ID: {sid[0]}, Name: {data['name']}, Courses: {', '.join(data['courses']) or 'None'}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
