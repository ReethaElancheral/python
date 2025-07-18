from tracker.parcel import update_status, get_status, list_all

def main():
    parcels = {}     
    cities = set()   

    while True:
        print("\nParcel Tracker")
        print("1. Update Parcel Status")
        print("2. Get Parcel Status")
        print("3. List All Parcels")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            tid = input("Enter Tracking ID: ").strip()
            city = input("Enter Current City: ").strip()
            status = input("Enter Status: ").strip()

            tracking_id = (tid,)  # Tuple ID
            update_status(parcels, cities, tracking_id, city, status)

        elif choice == "2":
            tid = input("Enter Tracking ID: ").strip()
            tracking_id = (tid,)
            get_status(parcels, tracking_id)

        elif choice == "3":
            list_all(parcels)

        elif choice == "4":
            print("Exiting Parcel Tracker.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
