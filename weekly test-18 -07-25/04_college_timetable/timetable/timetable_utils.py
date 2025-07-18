DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
PERIODS = [1, 2, 3, 4, 5]

def initialize_timetable():
    return {}  

def generate_timetable(subjects):
    timetable = {}
    for day in DAYS:
        used_subjects = set()
        for period in PERIODS:
            for subject in subjects:
                if subject not in used_subjects:
                    timetable[(day, period)] = subject
                    used_subjects.add(subject)
                    break
    return timetable

def print_timetable(timetable):
    print("\nGenerated Timetable:\n")
    for day in DAYS:
        print(f"{day}:")
        for period in PERIODS:
            slot = (day, period)
            subject = timetable.get(slot, "Free")
            print(f"  Period {period}: {subject}")
        print()
