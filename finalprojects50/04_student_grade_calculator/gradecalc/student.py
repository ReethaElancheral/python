from gradecalc.utils import memoize

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

        for subject, mark in marks.items():
            if not (0 <= mark <= 100):
                raise ValueError(f"Invalid mark {mark} for subject {subject}. Must be 0-100.")

    @memoize
    def calculate_gpa(self):
        total = sum(self.marks.values())
        count = len(self.marks)
        return total / count if count > 0 else 0

    def assign_grade(self):
        gpa = self.calculate_gpa()
        if gpa >= 90:
            return 'A'
        elif gpa >= 80:
            return 'B'
        elif gpa >= 70:
            return 'C'
        elif gpa >= 60:
            return 'D'
        elif gpa >= 50:
            return 'E'
        else:
            return 'F'

    def __str__(self):
        grades = f"GPA: {self.calculate_gpa():.2f}, Grade: {self.assign_grade()}"
        return f"ID: {self.student_id}, Name: {self.name}, {grades}"
