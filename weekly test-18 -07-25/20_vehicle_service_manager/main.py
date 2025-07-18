from service.service_manager import add_vehicle, update_services, show_vehicles

def main():
    service_db = {}

    while True:
        print("\nVehicle Service Manager")
        print("1. Add New Vehicle")
        print("2. Update Vehicle Services")
        print("3. Show All Vehicles")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            plate = input("Enter Plate Number: ").strip()
            owner = input("Enter Owner Name: ").strip()
            services = input("Enter services (comma separated): ").strip().split(",")
            services = [s.strip().capitalize() for s in services]
            add_vehicle(service_db, plate, owner, services)

        elif choice == "2":
            plate = input("Enter Plate Number: ").strip()
            new_services = input("Enter new services (comma separated): ").strip().split(",")
            new_services = [s.strip().capitalize() for s in new_services]
            update_services(service_db, plate, new_services)

        elif choice == "3":
            show_vehicles(service_db)

        elif choice == "4":
            print("Exiting Vehicle Service Manager.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
