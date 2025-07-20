def monthly_summary(weather_data):
    """Calculate average temperature and humidity from the log"""
    total_temp = 0
    total_humidity = 0
    count = len(weather_data)

    for temp, humidity, _ in weather_data.values():
        total_temp += temp
        total_humidity += humidity

    if count > 0:
        avg_temp = total_temp / count
        avg_humidity = total_humidity / count
        print(f"Average Temperature: {avg_temp:.1f}°C")
        print(f"Average Humidity: {avg_humidity:.1f}%")
    else:
        print("No weather data available.")

def unique_conditions(weather_data):
    """Extract and return all unique weather conditions from the log"""
    return set(condition for _, _, condition in weather_data.values())
