# 🧩 11. Result Card Generator

# Topics Covered: **kwargs, map(), lambda, conditionals
# Requirements:
# Input subject marks using **kwargs
# Use map() to grade each subject
# Return total, average, and status

def result_card_generator(**subjects):
    grade_func = lambda mark: (
        'A' if mark >= 90 else
        'B' if mark >= 80 else
        'C' if mark >= 70 else
        'D'
    )


    marks = subjects.values()

 
    grades = list(map(grade_func, marks))


    total = sum(marks)
    average = total / len(marks) if marks else 0


    status = "Pass"
    if any(mark < 35 for mark in marks):
        status = "Fail"
    elif average >= 90:
        status = "Excellent"
    elif average >= 75:
        status = "Good"
    elif average >= 50:
        status = "Average"
    else:
        status = "Poor"

    return {
        "Total": total,
        "Average": round(average, 2),
        "Grades": dict(zip(subjects.keys(), grades)),
        "Status": status
    }


result = result_card_generator(Math=95, English=88, Science=76, History=65, Art=45)

print("Result Card:")
for subject, grade in result["Grades"].items():
    print(f"{subject}: Grade {grade}")
print(f"Total Marks: {result['Total']}")
print(f"Average Marks: {result['Average']}")
print(f"Status: {result['Status']}")
