# gradesystem/report.py

from .marks import get_cgpa
from .grade import assign_grade

def generate_report(marks):
    cgpa = get_cgpa(marks)
    grades = [assign_grade(mark) for mark in marks]
    return cgpa, grades
