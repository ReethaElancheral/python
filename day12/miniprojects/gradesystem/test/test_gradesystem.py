# test/test_gradesystem.py

import unittest
from gradesystem.exceptions import InvalidMarkError, InvalidGradeError
from gradesystem.marks import get_cgpa
from gradesystem.grade import assign_grade
from gradesystem.report import generate_report

class TestGradeSystem(unittest.TestCase):

    def test_valid_cgpa(self):
        marks = [85, 90, 78]
        self.assertEqual(get_cgpa(marks), 84.33, places=2)

    def test_invalid_mark(self):
        marks = [105, 90, 78]
        with self.assertRaises(InvalidMarkError):
            get_cgpa(marks)

    def test_assign_grade(self):
        self.assertEqual(assign_grade(85), 'B')
        self.assertEqual(assign_grade(92), 'A')

    def test_invalid_grade(self):
        with self.assertRaises(InvalidGradeError):
            assign_grade(110)

    def test_generate_report(self):
        marks = [85, 90, 78]
        cgpa, grades = generate_report(marks)
        self.assertEqual(cgpa, 84.33, places=2)
        self.assertEqual(grades, ['B', 'A', 'C'])

if __name__ == '__main__':
    unittest.main()
