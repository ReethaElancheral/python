# weatherapp/weather.py

class Weather:
    def __init__(self, city, temp, humidity, description, forecast):
        self.city = city
        self.temp = temp        # Celsius
        self.humidity = humidity
        self.description = description
        self.forecast = forecast  # List of forecast dicts for next days

    def __str__(self):
        return (
            f"Weather in {self.city}:\n"
            f"Temperature: {self.temp:.1f}°C\n"
            f"Humidity: {self.humidity}%\n"
            f"Conditions: {self.description.capitalize()}"
        )

    def format_forecast(self):
        lines = [f"3-Day Forecast for {self.city}:"]
        for day in self.forecast:
            lines.append(f"{day['date']}: {day['temp']:.1f}°C, {day['description'].capitalize()}")
        return "\n".join(lines)
