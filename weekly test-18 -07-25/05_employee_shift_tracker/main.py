from shifts.shift_utils import assign_shift, display_shifts

def main():
    shift_registry = {}
    
    while True:
        print("\n=== Employee Shift Tracker ===")
        print("1. Assign Shift")
        print("2. View Shifts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            emp_id = tuple(input("Enter employee ID (e.g. E123): ").strip())
            name = input("Enter employee name: ").strip()
            shift = input("Enter shift (Morning/Evening/Night): ").strip().title()
            assign_shift(shift_registry, emp_id, name, shift)

        elif choice == "2":
            display_shifts(shift_registry)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
