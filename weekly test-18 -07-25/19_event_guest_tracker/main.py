from event.guest_utils import add_guest, view_event_guests, list_all_events

def main():
    events = {}  

    while True:
        print("\nEvent Guest Tracker")
        print("1. Add Guest")
        print("2. View Event Guests")
        print("3. List All Events")
        print("4. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            eid = input("Enter Event ID: ").strip()
            guest = input("Enter Guest Name: ").strip()
            rsvp = input("Enter RSVP (Yes/No/Maybe): ").strip()

            event_id = (eid,)  # Tuple
            add_guest(events, event_id, guest, rsvp)

        elif choice == "2":
            eid = input("Enter Event ID to view: ").strip()
            event_id = (eid,)
            view_event_guests(events, event_id)

        elif choice == "3":
            list_all_events(events)

        elif choice == "4":
            print("Exiting Guest Tracker.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
