def reserve_seat(user_id, name, seat_no, seats, occupied):
    if seat_no in occupied:
        print(f"Seat {seat_no} is already booked.")
        return

    occupied.add(seat_no)
    seats[seat_no] = {
        "user_id": user_id,
        "name": name
    }
    print(f"Seat {seat_no} reserved for {name} (User ID: {user_id}).")

def cancel_reservation(seat_no, seats, occupied):
    if seat_no in occupied:
        occupied.remove(seat_no)
        user = seats.pop(seat_no)
        print(f"Reservation for seat {seat_no} (User: {user['name']}) canceled.")
    else:
        print(f"Seat {seat_no} is not reserved.")

def view_reservations(seats):
    if not seats:
        print("No reservations yet.")
        return

    print("\n--- Reserved Seats ---")
    for seat, info in seats.items():
        print(f"Seat {seat} - {info['name']} (User ID: {info['user_id']})")
