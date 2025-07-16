# 20. Event Organizer

# Description: Organize event registrations.
# Requirements:
# - {event_name: {"participants": [...], "max": ...}}
# - Register participant (check max limit)
# - Cancel registration using remove()
# - Count participants per event


events = {}

def register(event_name, participant_name):
    """
    Register a participant for an event if there's capacity.
    Auto-creates the event if missing via setdefault.
    """
    event = events.setdefault(event_name, {"participants": [], "max": 0})
    if len(event["participants"]) >= event["max"]:
        print(f"❌ Cannot register {participant_name}; '{event_name}' is full.")
    elif participant_name in event["participants"]:
        print(f"❌ {participant_name} is already registered for '{event_name}'.")
    else:
        event["participants"].append(participant_name)
        print(f"✅ {participant_name} registered for '{event_name}'.")

def cancel_registration(event_name, participant_name):
    """Cancel a participant’s registration."""
    event = events.get(event_name)
    if event and participant_name in event["participants"]:
        event["participants"].remove(participant_name)
        print(f"✅ {participant_name}'s registration canceled for '{event_name}'.")
    else:
        print(f"❌ No registration found for {participant_name} in '{event_name}'.")

def set_event_capacity(event_name, max_participants):
    """Set or update the maximum participants for an event."""
    events.setdefault(event_name, {"participants": [], "max": 0})
    events[event_name]["max"] = max_participants
    print(f"📢 '{event_name}' capacity set to {max_participants} participants.")

def count_participants(event_name):
    """Return the current number of participants for an event."""
    event = events.get(event_name)
    count = len(event["participants"]) if event else 0
    print(f"ℹ️ '{event_name}' has {count} participants.")
    return count


set_event_capacity("AI Workshop", 3)
register("AI Workshop", "Alice")
register("AI Workshop", "Bob")
register("AI Workshop", "Charlie")
count_participants("AI Workshop")
register("AI Workshop", "David")  
cancel_registration("AI Workshop", "Bob")
count_participants("AI Workshop")
