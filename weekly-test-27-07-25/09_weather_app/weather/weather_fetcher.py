from .api import get_current_weather, get_5day_forecast
from .utils import celsius_to_fahrenheit

def format_current_weather(data, temp_unit="C"):
    if not data:
        return "No data available."
    name = data["name"]
    weather_desc = data["weather"][0]["description"].capitalize()
    temp_c = data["main"]["temp"]
    temp = temp_c
    unit_symbol = "°C"
    if temp_unit.upper() == "F":
        temp = celsius_to_fahrenheit(temp_c)
        unit_symbol = "°F"
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    result = (
        f"Current weather in {name}:\n"
        f"{weather_desc}\n"
        f"Temperature: {temp:.1f}{unit_symbol}\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s"
    )
    return result

def format_forecast(data, temp_unit="C"):
    if not data:
        return "No forecast data available."
    forecast_str = "5-Day Forecast:\n"
  
    forecasts = [item for item in data["list"] if "12:00:00" in item["dt_txt"]]
    for item in forecasts:
        date = item["dt_txt"].split()[0]
        desc = item["weather"][0]["description"].capitalize()
        temp_c = item["main"]["temp"]
        temp = temp_c
        unit_symbol = "°C"
        if temp_unit.upper() == "F":
            temp = celsius_to_fahrenheit(temp_c)
            unit_symbol = "°F"
        forecast_str += f"{date}: {desc}, Temp: {temp:.1f}{unit_symbol}\n"
    return forecast_str
