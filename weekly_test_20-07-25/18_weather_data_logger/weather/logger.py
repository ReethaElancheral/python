def add_weather(weather_data, date, info_tuple):
    """Add daily weather info"""
    weather_data[date] = info_tuple

def view_weather(weather_data):
    """Display stored weather data"""
    for date, (temp, humidity, condition) in sorted(weather_data.items()):
        print(f"{date} → Temp: {temp}°C, Humidity: {humidity}%, Condition: {condition}")
