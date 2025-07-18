from bus.bus_ops import reserve_seat, cancel_reservation, view_reservations

def main():
    seats = {}         
    occupied = set()   

    while True:
        print("\nBus Reservation System")
        print("1. Reserve Seat")
        print("2. Cancel Reservation")
        print("3. View Reservations")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            user_id = input("Enter User ID: ").strip()
            name = input("Enter Name: ").strip()
            seat_no = input("Enter Seat Number (e.g. A1): ").upper()

            reserve_seat((user_id,), name, seat_no, seats, occupied)

        elif choice == "2":
            seat_no = input("Enter Seat Number to cancel: ").upper()
            cancel_reservation(seat_no, seats, occupied)

        elif choice == "3":
            view_reservations(seats)

        elif choice == "4":
            print("Exiting Bus Reservation System.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
