# 8. Student Attendance Checker

# Goal: Mark students present using sets.
# Requirements:
# - Store enrolled and present students in sets.
# - Compare with difference() to find absentees.
# - Add latecomers using add() or update().
# Concepts Covered: Membership, add(), update(), set diff.

# Initial list of enrolled students
enrolled = {"alice", "bob", "carol", "dave", "eve"}
print("Enrolled students:", enrolled)

# Students who showed up initially
present = {"bob", "dave"}
print("Present initially:", present)

# 1. Find absentees using difference()
absentees = enrolled.difference(present)
print("Absent initially:", absentees)

# 2. Add latecomer(s)
present.add("carol")  
present.update(["alice", "frank"])  
print("Updated present list:", present)

# 3. Check membership
for student in ["eve", "frank"]:
    print(f"Is {student} present now?", student in present)

# 4. Final absentee check
final_absentees = enrolled.difference(present)
print("Final absentees:", final_absentees)
