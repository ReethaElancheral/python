# ✅ 2. Online Exam Result Evaluator

# Objective: Evaluate pass/fail and assign division.
# Requirements:
# Take 5 subject marks using a list.
# Use for loop to calculate total and percentage.
# Use conditions:
# If any subject < 35 → "Fail"
# Else use if-elif for grade based on percentage.


marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

failed = False
for m in marks:
    if m < 35:
        failed = True
        break

total = sum(marks)
percentage = total / len(marks)

print("\n🎓 Exam Result")
print(f"Marks     : {marks}")
print(f"Total     : {total}")
print(f"Percentage: {percentage:.2f}%")

if failed:
    print("Result    : ❌ Fail (One or more subjects below 35)")
else:
    print("Result    : ✅ Pass")
    if percentage > 75:
        print("Division  : Distinction")
    elif percentage >= 60 and percentage <=75:
        print("Division  : First Division")
    elif percentage >= 50 and percentage <60:
        print("Division  : Second Division")
    elif percentage >= 35 and percentage <50:
        print("Division  : Third Division")
