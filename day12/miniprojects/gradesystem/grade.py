# gradesystem/grade.py

from .exceptions import InvalidGradeError

GRADE_SCALE = {
    'A': (90, 100),
    'B': (80, 89),
    'C': (70, 79),
    'D': (60, 69),
    'F': (0, 59)
}

def assign_grade(mark):
    for grade, (lower, upper) in GRADE_SCALE.items():
        if lower <= mark <= upper:
            return grade
    raise InvalidGradeError(f"Invalid mark: {mark}")
