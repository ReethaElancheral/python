def update_status(parcels, cities, tracking_id, city, status):
    if tracking_id not in parcels:
        parcels[tracking_id] = {
            "status": status,
            "history": [city]
        }
        print(f"New parcel added with tracking ID {tracking_id}.")
    else:
        parcels[tracking_id]["status"] = status
        if city not in parcels[tracking_id]["history"]:
            parcels[tracking_id]["history"].append(city)
            print(f"City {city} added to parcel history.")

    cities.add(city)
    print(f"Updated status: {status}")

def get_status(parcels, tracking_id):
    if tracking_id in parcels:
        data = parcels[tracking_id]
        print(f"\nTracking ID: {tracking_id}")
        print(f"Current Status: {data['status']}")
        print(f"Cities Traveled: {', '.join(data['history'])}")
    else:
        print(f"No parcel found with tracking ID {tracking_id}.")

def list_all(parcels):
    if not parcels:
        print("No parcels being tracked.")
        return

    print("\n--- All Parcels ---")
    for tid, info in parcels.items():
        print(f"ID: {tid}, Status: {info['status']}, Cities: {', '.join(info['history'])}")
