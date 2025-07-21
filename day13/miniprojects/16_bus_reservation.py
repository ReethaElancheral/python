# 16. Bus Reservation System

# Concepts: Class, Composition, Magic Methods
# Classes:  Bus, Passenger,  Seat, Booking
# Requirements:
# Assign seats, check availability
# Use __eq__ for comparing bookings
# __str__ to display ticket

class Passenger:
    def __init__(self, passenger_id, name):
        self.passenger_id = passenger_id
        self.name = name

    def __str__(self):
        return f"Passenger: {self.name} (ID: {self.passenger_id})"

class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Seat {self.seat_number} - {status}"

class Booking:
    def __init__(self, passenger, seat):
        self.passenger = passenger
        self.seat = seat
        if not seat.is_booked:
            seat.is_booked = True
            print(f"Seat {seat.seat_number} booked for {passenger.name}")
        else:
            print(f"Seat {seat.seat_number} is already booked")

    def __eq__(self, other):
        if not isinstance(other, Booking):
            return False
        return (self.passenger.passenger_id == other.passenger.passenger_id and
                self.seat.seat_number == other.seat.seat_number)

    def __str__(self):
        return f"Booking - {self.passenger.name}, Seat: {self.seat.seat_number}"

class Bus:
    def __init__(self, bus_id, total_seats):
        self.bus_id = bus_id
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]
        self.bookings = []

    def check_seat_availability(self, seat_number):
        for seat in self.seats:
            if seat.seat_number == seat_number:
                return not seat.is_booked
        return False

    def book_seat(self, passenger, seat_number):
        if self.check_seat_availability(seat_number):
            seat = self.seats[seat_number - 1]
            booking = Booking(passenger, seat)
            self.bookings.append(booking)
            return booking
        else:
            print(f"Seat {seat_number} not available.")
            return None

    def __str__(self):
        booked_seats = [str(seat) for seat in self.seats if seat.is_booked]
        available_seats = [str(seat) for seat in self.seats if not seat.is_booked]
        return (f"Bus ID: {self.bus_id}\n"
                f"Booked Seats: {', '.join(booked_seats) if booked_seats else 'None'}\n"
                f"Available Seats: {', '.join(available_seats)}")

def main():
    bus = Bus("BUS123", 5)
    passenger1 = Passenger(1, "Nisha")
    passenger2 = Passenger(2, "Ravi")

    # Booking seats
    booking1 = bus.book_seat(passenger1, 2)
    booking2 = bus.book_seat(passenger2, 2)  # Should show already booked
    booking3 = bus.book_seat(passenger2, 3)

    # Compare bookings
    if booking1 and booking3:
        print(f"Booking1 equals Booking3? {booking1 == booking3}")

    # Display bookings and bus status
    print()
    print(booking1)
    print(booking3)
    print()
    print(bus)

if __name__ == "__main__":
    main()
