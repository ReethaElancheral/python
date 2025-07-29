# main.py

from weatherapp.manager import WeatherManager

def main():
    manager = WeatherManager()

    print("🌤️ Welcome to CLI Weather App")

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break

        weather = manager.fetch_weather(city)

        if weather:
            print(weather)
            print("3-Day Forecast:")
            for day in manager.weather_generator(city):
                print(f"{day['date']}: {day['temp']:.1f}°C, {day['description'].capitalize()}")

  
if __name__ == "__main__":
    main()
