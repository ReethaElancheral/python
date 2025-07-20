def add_appointment(appointments):
    date = input("Enter date (YYYY-MM-DD): ").strip()
    time = input("Enter time (e.g., 14:00): ").strip()
    person = input("Enter person's name: ").strip()
    purpose = input("Enter purpose: ").strip()

    appointment = (time, person, purpose)
    appointments.setdefault(date, []).append(appointment)
    print("Appointment added.")


def remove_appointment(appointments):
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if date not in appointments:
        print("No appointments found on that date.")
        return

    for idx, app in enumerate(appointments[date], 1):
        print(f"{idx}. {app[0]} with {app[1]} for {app[2]}")
    try:
        num = int(input("Enter appointment number to remove: "))
        if 1 <= num <= len(appointments[date]):
            removed = appointments[date].pop(num - 1)
            print(f"Removed appointment with {removed[1]}")
            if not appointments[date]:
                del appointments[date]
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")


def edit_appointment(appointments):
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if date not in appointments:
        print("No appointments on that date.")
        return

    for idx, app in enumerate(appointments[date], 1):
        print(f"{idx}. {app[0]} with {app[1]} for {app[2]}")
    try:
        num = int(input("Enter appointment number to edit: "))
        if 1 <= num <= len(appointments[date]):
            time = input("New time (leave blank to keep): ").strip()
            person = input("New person (leave blank to keep): ").strip()
            purpose = input("New purpose (leave blank to keep): ").strip()
            old_app = appointments[date][num - 1]

            updated = (
                time if time else old_app[0],
                person if person else old_app[1],
                purpose if purpose else old_app[2]
            )
            appointments[date][num - 1] = updated
            print("Appointment updated.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")
