from calendar_data import events
import calendar_data

def add_event(date, time, desc, participants):
    global_event_id = (date, time, calendar_data.event_counter)
    events[global_event_id] = {
        "date": date,
        "time": time,
        "desc": desc,
        "participants": set(participants)
    }
    calendar_data.event_counter += 1
    return global_event_id

def delete_event(event_id):
    if event_id in events:
        del events[event_id]
        return True
    return False

def update_event(event_id, new_desc=None, new_time=None, new_participants=None):
    if event_id in events:
        if new_desc:
            events[event_id]["desc"] = new_desc
        if new_time:
            events[event_id]["time"] = new_time
        if new_participants is not None:
            events[event_id]["participants"] = set(new_participants)
        return True
    return False
