def add_trip(trips):
    destination = input("Destination: ")
    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")
    participants = set(input("Participants (comma-separated): ").split(","))
    itinerary = input("Itinerary items (comma-separated): ").split(",")
    
    trip = {
        "destination": destination.strip(),
        "dates": (start.strip(), end.strip()),
        "participants": {p.strip() for p in participants},
        "itinerary": [item.strip() for item in itinerary],
    }
    trips.append(trip)
    print("Trip added successfully!")

def edit_trip(trips):
    view_trips(trips)
    index = int(input("Enter index to edit: "))
    if 0 <= index < len(trips):
        print("Leave blank to keep existing.")
        trip = trips[index]
        destination = input(f"Destination ({trip['destination']}): ") or trip["destination"]
        start = input(f"Start date ({trip['dates'][0]}): ") or trip["dates"][0]
        end = input(f"End date ({trip['dates'][1]}): ") or trip["dates"][1]
        participants = input("Participants (comma-separated, leave blank to keep): ")
        itinerary = input("Itinerary (comma-separated, leave blank to keep): ")

        trip["destination"] = destination
        trip["dates"] = (start, end)
        if participants:
            trip["participants"] = {p.strip() for p in participants.split(",")}
        if itinerary:
            trip["itinerary"] = [item.strip() for item in itinerary.split(",")]
        print("Trip updated.")
    else:
        print("Invalid index.")

def remove_trip(trips):
    view_trips(trips)
    index = int(input("Enter index to remove: "))
    if 0 <= index < len(trips):
        trips.pop(index)
        print("Trip removed.")
    else:
        print("Invalid index.")

def view_trips(trips):
    if not trips:
        print("No trips available.")
        return
    for i, trip in enumerate(trips):
        print(f"\nTrip {i}")
        print(f"Destination: {trip['destination']}")
        print(f"Dates: {trip['dates'][0]} to {trip['dates'][1]}")
        print(f"Participants: {', '.join(trip['participants'])}")
        print(f"Itinerary: {', '.join(trip['itinerary'])}")

def calculate_cost(trips):
    view_trips(trips)
    index = int(input("Enter trip index to calculate cost: "))
    if 0 <= index < len(trips):
        base_per_person = 10000  # INR
        num_people = len(trips[index]["participants"])
        total = base_per_person * num_people
        print(f"Estimated cost for {num_people} participants: ₹{total}")
    else:
        print("Invalid index.")
