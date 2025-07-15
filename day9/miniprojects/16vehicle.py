# 16. Vehicle Service History Tracker

# Goal: Maintain vehicle service history.
# Requirements:
# Each record: (vehicle_number, (service1_date, service2_date))
# Use slicing to show recent services.
# Unpack data to display timeline.
# Replace old tuple on new service.


service_history = [
    ("ABC123", ("2025-01-10", "2025-04-15")),
    ("XYZ456", ("2025-02-20", "2025-05-25")),
    ("LMN789", ("2025-03-30", "2025-06-05"))
]


def display_recent_services(service_history):
    print("\n🛠️ Recent Services (Last 2)")
    print("----------------------------")
    for vehicle_number, services in service_history:
        recent_services = services[-2:]  
        print(f"{vehicle_number}: {recent_services}")
    print("----------------------------")


def get_service_date(service_history, vehicle_number, service_index):
    for v_number, services in service_history:
        if v_number == vehicle_number:
            try:
                return services[service_index]
            except IndexError:
                print(f"Error: Service index {service_index} out of range.")
                return None
    print(f"Error: Vehicle '{vehicle_number}' not found.")
    return None


def add_service(service_history, vehicle_number, new_service_date):
    updated_history = []
    for v_number, services in service_history:
        if v_number == vehicle_number:
            services = (*services, new_service_date) 
        updated_history.append((v_number, services))
    return updated_history


display_recent_services(service_history)


vehicle_number = "ABC123"
service_index = 1 
service_date = get_service_date(service_history, vehicle_number, service_index)
if service_date:
    print(f"\n{vehicle_number}'s Service {service_index + 1} Date: {service_date}")


new_service_date = "2025-07-10"
service_history = add_service(service_history, vehicle_number, new_service_date)


print("\nUpdated Service History:")
display_recent_services(service_history)
