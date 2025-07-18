from timetable.timetable_utils import generate_timetable, print_timetable

def main():
    print("=== College Timetable Generator ===")

    subjects = set()
    try:
        n = int(input("Enter number of subjects: "))
    except ValueError:
        print("Invalid input.")
        return

    for i in range(n):
        subject = input(f"Enter subject #{i+1}: ").strip()
        subjects.add(subject)

    if not subjects:
        print("No subjects entered.")
        return

    timetable = generate_timetable(subjects)
    print_timetable(timetable)

if __name__ == "__main__":
    main()
