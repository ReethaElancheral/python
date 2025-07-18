# weather/formatter.py
def format_weather(data: dict) -> str:
    """Format weather data into a readable string."""
    city = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    return f"Weather in {city}:\n{description.capitalize()}\nTemperature: {temp}°C"
