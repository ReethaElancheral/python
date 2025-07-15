# 15. Movie Theater Booking

# Goal: Handle seating allocation in a theater.
# Requirements:
# Store seats as tuple of tuples: ((row1), (row2), ...)
# Access specific seat using seat[row][col].
# Show all empty seats using loop.
# Prevent changes to seats once booked using immutability.


seats = (
    ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"),
    ("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"),
    ("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"),
    ("D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"),
    ("E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"),
    ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10"),
    ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10")
)


def show_empty_seats(seats):
    print("\n🎟️ Available Seats")
    print("------------------------------")
    for row_num, row in enumerate(seats, start=1):
        for seat in row:
            print(f"Row {row_num}: {seat}")
    print("------------------------------")


def get_seat(seats, row, col):
    try:
        seat = seats[row-1][col-1]
        print(f"\n🎬 Seat {seat} is available.")
        return seat
    except IndexError:
        print("\n❌ Invalid seat position.")
        return None


def book_seat(seats, row, col):
    seat = get_seat(seats, row, col)
    if seat:
        print(f"\n✅ Seat {seat} booked successfully.")
     
        seats = tuple(
            tuple(seat if (r == row-1 and c == col-1) else seats[r][c] for c in range(len(seats[r])))
            for r in range(len(seats))
        )
        return seats
    return seats

# Display all empty seats
show_empty_seats(seats)

# Access a specific seat
get_seat(seats, 2, 3)

# Book a seat
seats = book_seat(seats, 2, 3)

# Display all empty seats after booking
show_empty_seats(seats)
