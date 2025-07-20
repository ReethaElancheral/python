from calendar_data import events

def list_dates_with_events():
    return sorted(set(event["date"] for event in events.values()))

def list_events_by_date(date):
    filtered = {eid: ev for eid, ev in events.items() if ev["date"] == date}
    if not filtered:
        print("No events found.")
    else:
        for eid, ev in filtered.items():
            print(f"\n🗓️ Event ID: {eid}")
            print(f"Time: {ev['time']}")
            print(f"Description: {ev['desc']}")
            print(f"Participants: {', '.join(ev['participants'])}")
