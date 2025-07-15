# 11. Flight Booking System

# Goal: Manage flight details and passengers using tuples.
# Requirements:
# Store each flight as: (flight_id, source, destination, (passenger_list))
# Show all passengers using nested loop and unpacking.
# Count number of passengers per flight.
# Update the flight by replacing with a new tuple.


flights = [
    (101, "Doha", "Dubai", ("Alice", "Bob")),
    (102, "Doha", "London", ("Charlie", "David")),
    (103, "Doha", "New York", ("Eve", "Frank", "Grace"))
]


def display_passengers(flights):
    print("\n🛫 Flight Passenger Lists")
    print("-------------------------------")
    for flight_id, source, destination, passengers in flights:
        print(f"Flight #{flight_id} ({source} → {destination}):")
        for passenger in passengers:
            print(f"  - {passenger}")
        print("-------------------------------")


def count_passengers(flights):
    print("\n👥 Passenger Count per Flight")
    print("-------------------------------")
    for flight_id, _, _, passengers in flights:
        print(f"Flight #{flight_id}: {len(passengers)} passengers")
    print("-------------------------------")


def update_flight(flight_id, new_details):
    global flights
    flights = [
        (new_details[0] if old_flight_id == flight_id else old_flight_id,
         source, destination, passengers)
        for old_flight_id, source, destination, passengers in flights
    ]
    print(f"\n🛠️ Flight #{flight_id} updated.")


display_passengers(flights)


count_passengers(flights)

update_flight(102, (102, "Doha", "Paris", ("Hannah", "Ivy")))


display_passengers(flights)
