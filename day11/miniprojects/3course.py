# 3. Course Enrollment Analyzer

# Goal: Compare students enrolled in two different courses.
# Requirements:
# - Store Python and Java student names in sets.
# - Find students enrolled in both (intersection).
# - Find exclusive Python students (difference).
# - Combine both courses (union).
# - Find students in only one course (symmetric_difference).
# Concepts Covered: union(), intersection(), difference(), symmetric_difference().


python_students = {"alice", "bob", "carol", "eve"}
java_students = {"bob", "dave", "carol", "frank"}

# 1. Intersection – students enrolled in both courses
both = python_students.intersection(java_students)

# 2. Difference – students only in Python
only_python = python_students.difference(java_students)

# 3. Union – all students enrolled in at least one course
all_students = python_students.union(java_students)

# 4. Symmetric Difference – students in exactly one course
exclusive = python_students.symmetric_difference(java_students)


print("Enrolled in both courses:", both)
print("Only Python students:", only_python)
print("All students:", all_students)
print("In exactly one course:", exclusive)
