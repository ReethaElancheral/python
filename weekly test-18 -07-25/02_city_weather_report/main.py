from weather_data.weather import fetch_weather, print_weather_report

def main():
    visited_cities = set()

    while True:
        print("\n--- City Weather Report (API) ---")
        print("1. Check Weather")
        print("2. View Visited Cities")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            city = input("Enter city name: ")
            try:
                lat = float(input("Enter latitude: "))
                lon = float(input("Enter longitude: "))
            except ValueError:
                print("Invalid coordinates.")
                continue

            coords = (lat, lon)
            visited_cities.add(city)

            weather = fetch_weather(city, coords)
            print_weather_report(weather)

        elif choice == '2':
            print("Visited Cities:", ", ".join(visited_cities) or "None")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
