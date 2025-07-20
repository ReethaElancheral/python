from scheduler.scheduler import add_appointment, remove_appointment, edit_appointment
from scheduler.notifier import display_schedule, list_unique_people

def main():
    appointments = {}

    while True:
        print("\n📅 Appointment Scheduler")
        print("1. Add Appointment")
        print("2. Remove Appointment")
        print("3. Edit Appointment")
        print("4. View Schedule")
        print("5. Show Unique People")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_appointment(appointments)
        elif choice == '2':
            remove_appointment(appointments)
        elif choice == '3':
            edit_appointment(appointments)
        elif choice == '4':
            display_schedule(appointments)
        elif choice == '5':
            list_unique_people(appointments)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
