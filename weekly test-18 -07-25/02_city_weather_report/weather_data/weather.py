import requests

API_KEY = "6b8475d1939bb5502208fc73e60459e5"

def fetch_weather(city, coords):
    lat, lon = coords
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return None

        return {
            "city": city,
            "temperature": f"{data['main']['temp']}°C",
            "condition": data['weather'][0]['main']
        }

    except Exception as e:
        print("Error fetching weather:", e)
        return None

def print_weather_report(weather):
    if not weather:
        print("No weather data to show.")
        return

    print(f"\nWeather Report for {weather['city']}")
    print(f"Temperature: {weather['temperature']}")
    print(f"Condition  : {weather['condition']}")
