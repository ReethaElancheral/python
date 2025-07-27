from weather.weather_fetcher import format_current_weather, format_forecast
from weather.api import get_current_weather, get_5day_forecast
from weather.favorites import add_favorite, remove_favorite, load_favorites
from weather.utils import celsius_to_fahrenheit, fahrenheit_to_celsius

def main():
    temp_unit = "C"
    print("🌤️ Weather App")

    while True:
        print("\nMenu:")
        print("1. Get current weather")
        print("2. Get 5-day forecast")
        print("3. Switch temperature unit (Currently °{})".format(temp_unit))
        print("4. Manage favorite locations")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            city = input("Enter city name: ")
            data = get_current_weather(city)
            print(format_current_weather(data, temp_unit))

        elif choice == "2":
            city = input("Enter city name: ")
            data = get_5day_forecast(city)
            print(format_forecast(data, temp_unit))

        elif choice == "3":
            temp_unit = "F" if temp_unit == "C" else "C"
            print(f"Temperature unit switched to °{temp_unit}")

        elif choice == "4":
            favs = load_favorites()
            print("Favorite locations:", favs if favs else "No favorites yet.")
            print("a. Add favorite")
            print("b. Remove favorite")
            sub_choice = input("Choose: ").lower()
            if sub_choice == "a":
                city = input("Enter city name to add: ")
                add_favorite(city)
                print(f"{city} added to favorites.")
            elif sub_choice == "b":
                city = input("Enter city name to remove: ")
                remove_favorite(city)
                print(f"{city} removed from favorites.")
            else:
                print("Invalid option.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
