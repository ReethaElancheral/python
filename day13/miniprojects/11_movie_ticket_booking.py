# 11. Movie Ticket Booking System

# Concepts: Class, Object, Polymorphism, Static Methods
# Classes:  Movie, Seat, Ticket, User
# Requirements:
# Show movies, book/cancel tickets
# Use @staticmethod to check seat availability
# Implement __str__ to display ticket details

class Movie:
    def __init__(self, movie_id, title, seats_available):
        self.movie_id = movie_id
        self.title = title
        self.seats_available = seats_available  # list of Seat objects

    def __str__(self):
        return f"Movie: {self.title} (ID: {self.movie_id})"

    def available_seats(self):
        return [seat for seat in self.seats_available if not seat.is_booked]

class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Seat {self.seat_number} booked.")
            return True
        else:
            print(f"Seat {self.seat_number} already booked.")
            return False

    def cancel(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Seat {self.seat_number} booking cancelled.")
            return True
        else:
            print(f"Seat {self.seat_number} is not booked yet.")
            return False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Seat {self.seat_number} - {status}"

class Ticket:
    def __init__(self, user, movie, seat):
        self.user = user
        self.movie = movie
        self.seat = seat
        if self.seat.book():
            print(f"Ticket booked for {self.user.name} - {self.movie.title} Seat: {self.seat.seat_number}")
        else:
            print("Booking failed.")

    def cancel_ticket(self):
        if self.seat.cancel():
            print(f"Ticket for {self.user.name} cancelled.")
        else:
            print("Cancellation failed.")

    def __str__(self):
        return f"Ticket: {self.movie.title} - Seat {self.seat.seat_number} for {self.user.name}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @staticmethod
    def check_seat_availability(movie, seat_number):
        for seat in movie.seats_available:
            if seat.seat_number == seat_number:
                return not seat.is_booked
        return False

def main():
    # Create seats
    seats = [Seat(i) for i in range(1, 11)]

    # Create movie
    movie = Movie(101, "Inception", seats)

    # Create user
    user = User(1, "Nisha")

    # Show available seats
    print(f"Available seats for {movie.title}:")
    for seat in movie.available_seats():
        print(seat)

    # Book a seat if available
    seat_number = 5
    if User.check_seat_availability(movie, seat_number):
        ticket = Ticket(user, movie, seats[seat_number - 1])
        print(ticket)
    else:
        print(f"Seat {seat_number} is not available.")

    # Cancel the ticket
    ticket.cancel_ticket()

    # Show seats after cancellation
    print(f"Seats after cancellation for {movie.title}:")
    for seat in movie.available_seats():
        print(seat)

if __name__ == "__main__":
    main()
