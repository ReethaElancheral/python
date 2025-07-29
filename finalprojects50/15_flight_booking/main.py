# 15. Flight Booking System 
# Objective: Book flights with seat selection. 
# Requirements: 
#  OOP: Flight class (destination, seats), Passenger class. 
#  List: Available seats (e.g., ["A1", "A2", ...]). 
#  File Handling: Save bookings to JSON. 
#  Exception Handling: Seat already booked. 
#  Functions: Book seat, cancel booking. 
#  Conditionals: Check seat availability. 
#  Loops: Display flight status. 
#  Set: Booked seats. 
#  Generator: Yield available seats. 
#  Decorator: @confirm_booking before finalizing. 


from booking.core import Flight, BookingManager

def main():
    print("✈️ Welcome to Flight Booking System")

    manager = BookingManager()

    # Add flights with seats
    manager.add_flight(Flight("New York"))
    manager.add_flight(Flight("London"))
    manager.add_flight(Flight("Tokyo"))

    while True:
        print("\nMenu:")
        print("1. Show Flights Status")
        print("2. Book a Seat")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            manager.display_flights()

        elif choice == '2':
            name = input("Enter passenger name: ").strip()
            dest = input("Enter flight destination: ").strip()
            seat = input("Enter seat (e.g., A1): ").strip()
            manager.book_seat(name, dest, seat)

        elif choice == '3':
            name = input("Enter passenger name: ").strip()
            dest = input("Enter flight destination: ").strip()
            seat = input("Enter seat to cancel: ").strip()
            manager.cancel_booking(name, dest, seat)

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
