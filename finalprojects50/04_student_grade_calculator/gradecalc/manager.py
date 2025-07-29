# gradecalc/manager.py

import csv
from gradecalc.student import Student

class StudentManager:
    def __init__(self):
        self.students = {}  # key: student_id, value: Student object

    def add_student(self, student_id, name, marks):
        if student_id in self.students:
            print("Student ID already exists.")
            return
        try:
            student = Student(student_id, name, marks)
            self.students[student_id] = student
            print("Student added successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def compute_class_average(self):
        if not self.students:
            return 0
        total_gpa = sum(s.calculate_gpa() for s in self.students.values())
        return total_gpa / len(self.students)

    def find_top_student(self):
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.calculate_gpa())

    def export_grades_csv(self, filename="grades.csv"):
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            header = ["ID", "Name", "GPA", "Grade"]
            writer.writerow(header)
            for student in self.students.values():
                writer.writerow([
                    student.student_id,
                    student.name,
                    f"{student.calculate_gpa():.2f}",
                    student.assign_grade()
                ])
        print(f"Grades exported to {filename}")

    def unique_subjects(self):
        subjects = set()
        for student in self.students.values():
            subjects.update(student.marks.keys())
        return subjects

    def yield_students_with_grade_a(self):
        for student in self.students.values():
            if student.assign_grade() == 'A':
                yield student

    def display_all_students(self):
        if not self.students:
            print("No students added yet.")
            return
        for student in self.students.values():
            print(student)
