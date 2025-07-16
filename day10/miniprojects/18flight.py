# 18. Flight Booking System

# Description: Manage passenger bookings for flights.
# Requirements:
# - {flight_id: {"route": ..., "passengers": [...]} }
# - Add/remove passengers
# - Check seat availability
# - Use .setdefault() to auto-create flights


flights = {}

def add_passenger(flight_id, passenger_name, route=None):
    """
    Add a passenger to a flight.
    If the flight doesn't exist, auto-create using setdefault().
    """
    flight = flights.setdefault(
        flight_id,
        {"route": route or "Unknown", "passengers": []}
    )
    if passenger_name not in flight["passengers"]:
        flight["passengers"].append(passenger_name)
        print(f"{passenger_name} added to flight {flight_id}.")
    else:
        print(f"{passenger_name} is already on flight {flight_id}.")

def remove_passenger(flight_id, passenger_name):
    """Remove a passenger if they exist on the flight."""
    flight = flights.get(flight_id)
    if flight and passenger_name in flight["passengers"]:
        flight["passengers"].remove(passenger_name)
        print(f"{passenger_name} removed from flight {flight_id}.")
    else:
        print(f"{passenger_name} not found on flight {flight_id}.")

def check_availability(flight_id, max_seats):
    """Return available seats based on maximum capacity."""
    flight = flights.get(flight_id)
    if flight:
        available = max_seats - len(flight["passengers"])
        print(f"Flight {flight_id} has {available} available seats.")
        return available
    else:
        print(f"Flight {flight_id} does not exist.")
        return 0

def list_passengers(flight_id):
    """List all passengers on the given flight."""
    flight = flights.get(flight_id)
    if flight:
        print(f"Passengers on flight {flight_id}: {', '.join(flight['passengers'])}")
    else:
        print(f"Flight {flight_id} does not exist.")

add_passenger("AI202", "Alice", route="Doha → Mumbai")
add_passenger("AI202", "Bob")
add_passenger("AI202", "Alice")  
remove_passenger("AI202", "Alice")
check_availability("AI202", max_seats=100)
list_passengers("AI202")
