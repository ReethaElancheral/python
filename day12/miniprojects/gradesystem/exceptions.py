# gradesystem/exceptions.py

class InvalidMarkError(Exception):
    """Raised when a mark is outside the valid range (0-100)."""
    pass

class InvalidGradeError(Exception):
    """Raised when a grade is not recognized."""
    pass
