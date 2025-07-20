from event_ops import add_event, delete_event, update_event
from calendar_view import list_dates_with_events, list_events_by_date
from calendar_data import events

def main():
    while True:
        print("\n--- Simple Calendar App ---")
        print("1. Add Event")
        print("2. Delete Event")
        print("3. Update Event")
        print("4. List Dates with Events")
        print("5. List Events by Date")
        print("6. Show All Events")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            desc = input("Enter description: ")
            participants = input("Enter participants (comma separated): ").split(",")
            event_id = add_event(date, time, desc, [p.strip() for p in participants])
            print(f"✅ Event added with ID: {event_id}")

        elif choice == "2":
            event_id = eval(input("Enter event ID (tuple): "))
            if delete_event(event_id):
                print("✅ Event deleted.")
            else:
                print("❌ Event not found.")

        elif choice == "3":
            event_id = eval(input("Enter event ID (tuple): "))
            new_desc = input("New description (leave blank to skip): ") or None
            new_time = input("New time (leave blank to skip): ") or None
            new_participants = input("New participants (comma separated, blank to skip): ")
            new_participants = [p.strip() for p in new_participants.split(",")] if new_participants else None
            if update_event(event_id, new_desc, new_time, new_participants):
                print("✅ Event updated.")
            else:
                print("❌ Event not found.")

        elif choice == "4":
            dates = list_dates_with_events()
            print("\n📅 Dates with events:")
            for d in dates:
                print(d)

        elif choice == "5":
            date = input("Enter date to search (YYYY-MM-DD): ")
            list_events_by_date(date)

        elif choice == "6":
            print("\n📘 All Events:")
            for eid, ev in events.items():
                print(f"{eid}: {ev}")

        elif choice == "0":
            print("Exiting Calendar App.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
