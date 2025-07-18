def add_booking(passenger_id, name, destination, bookings, destinations):
    pid = (passenger_id,)  # Tuple as ID

    if pid in bookings:
        print(f"Passenger {passenger_id} already booked a flight.")
        return

    bookings[pid] = {
        "name": name,
        "destination": destination
    }

    destinations.add(destination)
    print(f"Booking confirmed for {name} to {destination}.")
