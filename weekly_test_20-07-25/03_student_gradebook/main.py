

from gradebook.student_ops import add_student, update_grade, get_all_subjects
from gradebook.report_gen import print_report_card, top_scorer

students = [
    {
        "id": (101, "Alice"),
        "grades": {"Math": 85, "Science": 90}
    },
    {
        "id": (102, "Bob"),
        "grades": {"Math": 78, "English": 88}
    }
]

def main():
    while True:
        print("\n1. Add Student  2. Update Grade  3. Show Reports  4. Topper  5. Subjects  6. Exit")
        ch = input("Choice: ")

        if ch == "1":
            roll = int(input("Roll No: "))
            name = input("Name: ")
            add_student(roll, name, students)

        elif ch == "2":
            roll = int(input("Roll No: "))
            sub = input("Subject: ")
            grade = int(input("Grade: "))
            if not update_grade(roll, sub, grade, students):
                print("Student not found.")

        elif ch == "3":
            print_report_card(students)

        elif ch == "4":
            top, avg = top_scorer(students)
            if top:
                print(f"\nTop Performer: {top['id'][1]} with Avg: {avg:.2f}")

        elif ch == "5":
            subjects = get_all_subjects(students)
            print("\nSubjects offered:", ", ".join(subjects))

        elif ch == "6":
            break

if __name__ == "__main__":
    main()
