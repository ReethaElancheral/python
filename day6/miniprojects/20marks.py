# 🧩 20. Marks to Grade Converter

# Topics Covered: map(), lambda, list, return
# Requirements:
# Accept list of marks
# Convert to grade using conditions (A, B, etc.)
# Return final graded list

def marks_to_grades(marks):

    grade_func = lambda m: (
        'A' if m >= 90 else
        'B' if m >= 80 else
        'C' if m >= 70 else
        'D'
    )
  
    grades = list(map(grade_func, marks))
    return grades


marks_list = [95, 82, 67, 74, 88, 91, 53]
grades_list = marks_to_grades(marks_list)
print(grades_list)  
