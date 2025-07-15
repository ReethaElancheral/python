# 8. Bus Schedule Management System

# Goal: Handle route schedules using tuples.
# Requirements:
# Store route as (bus_no, departure_time, arrival_time, (stops))
# Use slicing and indexing to extract time and stops.
# Display entire schedule using unpacking.
# Simulate update by replacing old tuple with a new one.



bus_schedule = [
    (101, "08:00", "10:00", ("Station A", "Station B", "Station C")),
    (102, "09:00", "11:00", ("Station D", "Station E", "Station F")),
    (103, "10:00", "12:00", ("Station G", "Station H", "Station I"))
]

def display_schedule(schedule):
    print("\n🚌 Bus Schedule")
    print("-------------------------------")
    for bus_no, dep_time, arr_time, stops in schedule:
        print(f"Bus #{bus_no} | Departs: {dep_time} | Arrives: {arr_time}")
        print("Stops:", " → ".join(stops))
        print("-------------------------------")

def update_schedule(bus_no, new_schedule):
    global bus_schedule
    bus_schedule = [
        (new_schedule[0] if old_bus_no == bus_no else old_bus_no,
         dep_time, arr_time, stops)
        for old_bus_no, dep_time, arr_time, stops in bus_schedule
    ]
    print(f"\n🛠️ Schedule for Bus #{bus_no} updated.")


display_schedule(bus_schedule)


update_schedule(102, (102, "09:30", "11:30", ("Station D", "Station E", "Station G")))


display_schedule(bus_schedule)

