def add_guest(events, event_id, guest_name, rsvp_status):
    if event_id not in events:
        events[event_id] = {
            "guests": set(),
            "rsvp": {}
        }

    if guest_name in events[event_id]["guests"]:
        print(f"{guest_name} is already added to event {event_id}.")
        return

    events[event_id]["guests"].add(guest_name)
    events[event_id]["rsvp"][guest_name] = rsvp_status
    print(f"Guest '{guest_name}' added to Event {event_id} with RSVP: {rsvp_status}.")

def view_event_guests(events, event_id):
    if event_id not in events:
        print(f"No such event {event_id}.")
        return

    print(f"\n--- Guests for Event {event_id} ---")
    for guest in events[event_id]["guests"]:
        status = events[event_id]["rsvp"].get(guest, "Unknown")
        print(f"{guest} - RSVP: {status}")

def list_all_events(events):
    if not events:
        print("No events tracked yet.")
        return

    print("\nTracked Events:")
    for event_id in events:
        print(f"- Event {event_id}")
