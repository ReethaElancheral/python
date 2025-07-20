def display_schedule(appointments):
    if not appointments:
        print("No appointments scheduled.")
        return

    print("\n--- Schedule ---")
    for date in sorted(appointments.keys()):
        print(f"\n📆 {date}")
        for time, person, purpose in sorted(appointments[date]):
            print(f"🕒 {time} - {person} ({purpose})")


def list_unique_people(appointments):
    people = set()
    for date_apps in appointments.values():
        for _, person, _ in date_apps:
            people.add(person)

    print("\n👥 Unique People in Schedule:")
    if people:
        for p in sorted(people):
            print(f"• {p}")
    else:
        print("No appointments yet.")
