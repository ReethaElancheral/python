# 12. Weather Report Generator

# Concepts: f-strings, +, .format()
# Input: city, temperature (°C), humidity
# Output: "Weather in Chennai: 35°C, 60% humidity" using all 3 formatting methods


city = input("Enter city name: ").strip()
temperature = input("Enter temperature (°C): ").strip()
humidity = input("Enter humidity (%): ").strip()

report_fstring = f"Weather in {city}: {temperature}°C, {humidity}% humidity"

report_plus = "Weather in " + city + ": " + temperature + "°C, " + humidity + "% humidity"

report_format = "Weather in {}: {}°C, {}% humidity".format(city, temperature, humidity)

print("\n--- Weather Reports ---")
print("F-string:     ", report_fstring)
print("Concatenation:", report_plus)
print("Format():     ", report_format)
