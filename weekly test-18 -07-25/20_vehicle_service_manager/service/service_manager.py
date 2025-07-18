def add_vehicle(service_db, plate_number, owner_name, service_list):
    plate = (plate_number,)  # Make it immutable tuple

    if plate in service_db:
        print(f"Vehicle {plate_number} already exists.")
        return

    service_db[plate] = {
        "owner": owner_name,
        "services": set(service_list)
    }
    print(f"Vehicle {plate_number} added for services: {', '.join(service_list)}.")

def update_services(service_db, plate_number, new_services):
    plate = (plate_number,)
    
    if plate not in service_db:
        print(f"No vehicle found with plate {plate_number}.")
        return

    service_db[plate]["services"].update(new_services)
    print(f"Updated services for {plate_number}: {', '.join(service_db[plate]['services'])}")

def show_vehicles(service_db):
    if not service_db:
        print("No vehicles in service database.")
        return

    print("\n--- Vehicle Service Records ---")
    for plate, info in service_db.items():
        print(f"Plate: {plate[0]}")
        print(f"Owner: {info['owner']}")
        print(f"Services: {', '.join(info['services'])}")
        print("-" * 30)
