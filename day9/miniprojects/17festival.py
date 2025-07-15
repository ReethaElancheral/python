# 17. Festival Event Planner

# Goal: Plan festival events with tuple-based scheduling.
# Requirements:
# Store event as (event_name, (start_time, end_time, location))
# Display schedule with index-based access.
# Use list of tuples to show full day plan.
# Immutable tuples prevent accidental time edits.


event_schedule = [
    ("Morning Yoga", ("08:00", "09:00", "Beachside Stage")),
    ("Art Exhibition", ("09:30", "11:00", "Gallery Hall")),
    ("Cooking Workshop", ("11:30", "13:00", "Culinary Tent")),
    ("Live Band Performance", ("14:00", "15:30", "Main Stage")),
    ("Dance Class", ("16:00", "17:00", "Dance Pavilion"))
]


def display_full_day_schedule(schedule):
    print("\n🎟️ Full Day Event Schedule")
    print("----------------------------")
    for index, (event_name, (start_time, end_time, location)) in enumerate(schedule, start=1):
        print(f"{index}. {event_name} | {start_time} - {end_time} | {location}")
    print("----------------------------")


def get_event_by_index(schedule, index):
    try:
        event_name, (start_time, end_time, location) = schedule[index - 1]
        return f"{event_name} | {start_time} - {end_time} | {location}"
    except IndexError:
        return "❌ Invalid event index."


display_full_day_schedule(event_schedule)


event_index = 3  
event_info = get_event_by_index(event_schedule, event_index)
print(f"\nEvent at index {event_index}: {event_info}")
