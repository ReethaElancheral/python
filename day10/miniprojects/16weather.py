# 16. Weather Report Analyzer

# Description: Store temperature data by city.
# Requirements:
# - Structure: {city_name: [temps]}
# - Add new temperature each day
# - Calculate average per city
# - Sort cities by hottest average


weather_data = {
    "Doha": [42, 43, 44, 45],
    "Paris": [18, 19, 20, 21],
    "New York": [25, 26, 27, 28],
}

def add_temperature(city_name, temp):
    """Add a new temperature reading for a city."""
    if city_name in weather_data:
        weather_data[city_name].append(temp)
    else:
        weather_data[city_name] = [temp]

def calculate_average(city_name):
    """Calculate the average temperature for a city."""
    temps = weather_data.get(city_name)
    if temps:
        return sum(temps) / len(temps)
    else:
        return None

def sort_cities_by_average():
    """Sort cities by average temperature in descending order."""
    return sorted(weather_data.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)


add_temperature("Doha", 46)
add_temperature("Paris", 22)
add_temperature("New York", 29)

print("Average Temperatures:")
for city, temps in weather_data.items():
    print(f"{city}: {calculate_average(city):.2f}°C")

print("\nCities Sorted by Hottest Average Temperature:")
for city, temps in sort_cities_by_average():
    print(f"{city}: {calculate_average(city):.2f}°C")
