from flight.booking import add_booking
from flight.payment import process_payment

def main():
    bookings = {}
    destinations = set()

    while True:
        print("\n1. Book Flight")
        print("2. View Bookings")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            pid = input("Enter Passenger ID: ").strip()
            name = input("Enter Name: ").strip()
            destination = input("Enter Destination: ").strip().title()
            amount = float(input("Enter amount to pay: "))

            process_payment(pid, amount)
            add_booking(pid, name, destination, bookings, destinations)

        elif choice == "2":
            if not bookings:
                print("No bookings yet.")
                continue
            print("\nAll Bookings:")
            for pid, info in bookings.items():
                print(f"Passenger {info['name']} -> {info['destination']}")

            print(f"\nUnique destinations: {', '.join(destinations)}")

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
