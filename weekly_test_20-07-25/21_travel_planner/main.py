from planner.trip_ops import add_trip, edit_trip, remove_trip, view_trips, calculate_cost
from planner.suggestion_engine import suggest_destinations

def main():
    trips = []
    while True:
        print("\n--- Travel Planner ---")
        print("1. Add Trip")
        print("2. Edit Trip")
        print("3. Remove Trip")
        print("4. View Trips")
        print("5. Suggest Destinations")
        print("6. Calculate Trip Cost")
        print("0. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_trip(trips)
        elif choice == "2":
            edit_trip(trips)
        elif choice == "3":
            remove_trip(trips)
        elif choice == "4":
            view_trips(trips)
        elif choice == "5":
            suggest_destinations(trips)
        elif choice == "6":
            calculate_cost(trips)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
