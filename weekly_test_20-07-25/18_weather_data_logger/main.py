from weather.logger import add_weather, view_weather
from weather.analysis import monthly_summary, unique_conditions

if __name__ == "__main__":
    weather_log = {}

   
    add_weather(weather_log, "2025-07-17", (36, 55, "Sunny"))
    add_weather(weather_log, "2025-07-18", (34, 65, "Cloudy"))
    add_weather(weather_log, "2025-07-19", (37, 60, "Sunny"))
    add_weather(weather_log, "2025-07-20", (33, 70, "Rainy"))

    print("\n📆 Weather Log:")
    view_weather(weather_log)

    print("\n📊 Monthly Summary:")
    monthly_summary(weather_log)

    print("\n🌦️ Unique Conditions:")
    print(unique_conditions(weather_log))
