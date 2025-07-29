import json
import os

from .decorators import confirm_booking

class Flight:
    def __init__(self, destination, seats=None):
        self.destination = destination
        # Initialize seats like ["A1", "A2", ...] if none provided
        self.seats = seats if seats else [f"A{i}" for i in range(1, 11)]
        self.booked_seats = set()

    def available_seats_generator(self):
        for seat in self.seats:
            if seat not in self.booked_seats:
                yield seat

    def is_seat_available(self, seat):
        return seat in self.seats and seat not in self.booked_seats

    def book_seat(self, seat):
        if self.is_seat_available(seat):
            self.booked_seats.add(seat)
            return True
        else:
            raise ValueError(f"Seat {seat} is already booked or invalid.")

    def cancel_seat(self, seat):
        if seat in self.booked_seats:
            self.booked_seats.remove(seat)
            return True
        else:
            raise ValueError(f"Seat {seat} is not booked.")

    def display_status(self):
        print(f"Flight to {self.destination}")
        print(f"Total seats: {len(self.seats)}")
        print(f"Booked seats: {sorted(self.booked_seats)}")
        print(f"Available seats: {sorted(set(self.seats) - self.booked_seats)}")

class Passenger:
    def __init__(self, name, flight, seat):
        self.name = name
        self.flight = flight
        self.seat = seat

class BookingManager:
    def __init__(self, booking_file="booking/bookings.json"):
        self.booking_file = booking_file
        self.flights = {}
        self.passengers = []
        self.load_bookings()

    def add_flight(self, flight):
        self.flights[flight.destination] = flight

    @confirm_booking
    def book_seat(self, passenger_name, flight_dest, seat):
        flight = self.flights.get(flight_dest)
        if not flight:
            print(f"⚠️ Flight to {flight_dest} not found.")
            return False
        try:
            flight.book_seat(seat)
        except ValueError as e:
            print(f"⚠️ {e}")
            return False
        passenger = Passenger(passenger_name, flight_dest, seat)
        self.passengers.append(passenger)
        self.save_bookings()
        print(f"✅ Seat {seat} booked for {passenger_name} on flight to {flight_dest}.")
        return True

    def cancel_booking(self, passenger_name, flight_dest, seat):
        flight = self.flights.get(flight_dest)
        if not flight:
            print(f"⚠️ Flight to {flight_dest} not found.")
            return False
        try:
            flight.cancel_seat(seat)
        except ValueError as e:
            print(f"⚠️ {e}")
            return False
        # Remove passenger booking
        self.passengers = [p for p in self.passengers if not (
            p.name == passenger_name and p.flight == flight_dest and p.seat == seat)]
        self.save_bookings()
        print(f"✅ Booking cancelled for {passenger_name}, seat {seat}, flight {flight_dest}.")
        return True

    def display_flights(self):
        for flight in self.flights.values():
            flight.display_status()
            print("-" * 30)

    def save_bookings(self):
        data = []
        for p in self.passengers:
            data.append({
                "name": p.name,
                "flight": p.flight,
                "seat": p.seat
            })
        with open(self.booking_file, 'w') as f:
            json.dump(data, f)

    def load_bookings(self):
        if not os.path.exists(self.booking_file):
            return
        try:
            with open(self.booking_file, 'r') as f:
                data = json.load(f)
            # Rebuild passengers and update booked seats
            self.passengers.clear()
            for record in data:
                p = Passenger(record["name"], record["flight"], record["seat"])
                self.passengers.append(p)
                flight = self.flights.get(p.flight)
                if flight:
                    flight.booked_seats.add(p.seat)
        except Exception as e:
            print(f"⚠️ Failed to load bookings: {e}")
