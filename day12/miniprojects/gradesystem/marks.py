# gradesystem/marks.py

from .exceptions import InvalidMarkError
from .utils import calculate_cgpa

def validate_marks(marks):
    if not all(0 <= mark <= 100 for mark in marks):
        raise InvalidMarkError("Marks must be between 0 and 100.")

def get_cgpa(marks):
    validate_marks(marks)
    return calculate_cgpa(marks)
