# main.py

# 4. Student Grade Calculator 
# Objective: Compute student grades (A-F) based on marks. 
# Requirements: 
#  OOP: Student class (name, marks). 
#  Dictionary: Store students (key: ID, value: Student object). 
#  File Handling: Export grades to CSV. 
#  Exception Handling: Invalid marks (0-100). 
#  Functions: Calculate GPA, find top student. 
#  Conditionals: Assign grades (if-elif-else). 
#  Loops: Compute class average. 
#  Set: Unique subjects. 
#  Generator: Yield students with grade 'A'. 
#  Decorator: @memoize to cache GPA calculations.


from gradecalc.manager import StudentManager

def input_marks():
    marks = {}
    print("Enter marks for subjects. Type 'done' to finish.")
    while True:
        subj = input("Subject name (or 'done'): ").strip()
        if subj.lower() == 'done':
            break
        try:
            mark = float(input(f"Mark for {subj}: "))
            if not 0 <= mark <= 100:
                print("Mark must be between 0 and 100.")
                continue
            marks[subj] = mark
        except ValueError:
            print("Please enter a valid number for mark.")
    return marks

def main():
    manager = StudentManager()

    while True:
        print("\n🎓 Student Grade Calculator")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Compute Class Average GPA")
        print("4. Find Top Student")
        print("5. Export Grades to CSV")
        print("6. Show Unique Subjects")
        print("7. Show Students with Grade 'A'")
        print("8. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            student_id = input("Student ID: ").strip()
            name = input("Student Name: ").strip()
            marks = input_marks()
            manager.add_student(student_id, name, marks)

        elif choice == '2':
            manager.display_all_students()

        elif choice == '3':
            avg = manager.compute_class_average()
            print(f"Class Average GPA: {avg:.2f}")

        elif choice == '4':
            top_student = manager.find_top_student()
            if top_student:
                print("Top Student:")
                print(top_student)
            else:
                print("No students found.")

        elif choice == '5':
            filename = input("Enter filename to export (default: grades.csv): ").strip()
            if not filename:
                filename = "grades.csv"
            manager.export_grades_csv(filename)

        elif choice == '6':
            subjects = manager.unique_subjects()
            if subjects:
                print("Unique Subjects:")
                for s in subjects:
                    print(f"- {s}")
            else:
                print("No subjects found.")

        elif choice == '7':
            print("Students with Grade 'A':")
            found = False
            for student in manager.yield_students_with_grade_a():
                print(student)
                found = True
            if not found:
                print("No students with grade 'A' found.")

        elif choice == '8':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
