# 2. School Report Card Generator

# Concepts: Class, Inheritance, Class Methods, Encapsulation, Overriding
# Classes:  Person, Student, Teacher, Subject, ReportCard
# Requirements:
# Generate grade report per subject per student
# Teacher updates marks
# Access student info securely
# Use polymorphism to handle different grading systems

class Person:
    def __init__(self, name, age):
        self._name = name         # Encapsulated (protected)
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self._subjects = {}  # subject_name -> marks

    def add_subject(self, subject):
        self._subjects[subject.name] = None  # Marks not set initially

    def set_marks(self, subject_name, marks):
        if subject_name in self._subjects:
            self._subjects[subject_name] = marks
        else:
            print(f"Subject '{subject_name}' not found for this student.")

    def get_marks(self):
        return self._subjects.copy()

    def __str__(self):
        return f"Student: {self._name}, ID: {self.student_id}"

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def update_marks(self, student, subject_name, marks):
        student.set_marks(subject_name, marks)

    def __str__(self):
        return f"Teacher: {self._name}, Employee ID: {self.employee_id}"

class Subject:
    def __init__(self, name):
        self.name = name

    def grading_system(self, marks):
        # Base grading (can be overridden for polymorphism)
        if marks >= 90:
            return 'A+'
        elif marks >= 80:
            return 'A'
        elif marks >= 70:
            return 'B+'
        elif marks >= 60:
            return 'B'
        elif marks >= 50:
            return 'C'
        else:
            return 'F'

class ReportCard:
    def __init__(self, student):
        self.student = student

    def generate_report(self, subjects):
        print(f"Report Card for {self.student}")
        for subject in subjects:
            marks = self.student.get_marks().get(subject.name)
            if marks is not None:
                grade = subject.grading_system(marks)  # Polymorphism: grading_system could differ per subject
                print(f"{subject.name}: Marks = {marks}, Grade = {grade}")
            else:
                print(f"{subject.name}: Marks not available")

# Example polymorphism: Science uses different grading system
class ScienceSubject(Subject):
    def grading_system(self, marks):
        # Different scale for Science 
        if marks >= 85:
            return 'Distinction'
        elif marks >= 70:
            return 'First Class'
        elif marks >= 50:
            return 'Pass'
        else:
            return 'Fail'


def main():
    
    student1 = Student("Nisha", 15, "S101")
    teacher1 = Teacher("Mr. Sharma", 40, "T202")

    # Subjects
    math = Subject("Math")
    english = Subject("English")
    science = ScienceSubject("Science")  # Uses polymorphic grading

    subjects = [math, english, science]

    # Add subjects to student
    for sub in subjects:
        student1.add_subject(sub)

    # Teacher updates marks
    teacher1.update_marks(student1, "Math", 88)
    teacher1.update_marks(student1, "English", 76)
    teacher1.update_marks(student1, "Science", 82)

    # Generate report card
    report = ReportCard(student1)
    report.generate_report(subjects)

if __name__ == "__main__":
    main()
