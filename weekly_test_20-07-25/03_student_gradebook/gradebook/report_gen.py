

def print_report_card(students):
    for s in students:
        sid = s["id"]
        grades = s["grades"]
        avg = sum(grades.values()) / len(grades) if grades else 0
        print(f"\nReport Card: {sid[1]} (Roll No: {sid[0]})")
        for subject, mark in grades.items():
            print(f"  {subject}: {mark}")
        print(f"  Average: {avg:.2f}")

def top_scorer(students):
    top_student = None
    top_avg = 0
    for s in students:
        grades = s["grades"]
        if grades:
            avg = sum(grades.values()) / len(grades)
            if avg > top_avg:
                top_avg = avg
                top_student = s
    return top_student, top_avg
