from grades.grade_utils import add_student_marks, display_grades

def main():
    gradebook = {}

    while True:
        print("\n=== Student Grade Calculator ===")
        print("1. Add Student Marks")
        print("2. View Grades")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Enter Student ID: ").strip()

            try:
                n = int(input("Number of subjects: "))
                subjects = set()
                subjects_marks = {}

                for _ in range(n):
                    subject = input("Subject name: ").strip().title()
                    if subject in subjects:
                        print("Duplicate subject! Skipping.")
                        continue
                    mark = float(input(f"Mark in {subject}: "))
                    subjects.add(subject)
                    subjects_marks[subject] = mark

                add_student_marks(gradebook, student_id, subjects_marks)

            except ValueError:
                print("Invalid input. Try again.")

        elif choice == '2':
            display_grades(gradebook)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
