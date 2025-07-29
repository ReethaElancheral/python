# weatherapp/manager.py

import requests
from weatherapp.weather import Weather
from weatherapp.utils import retry
from datetime import datetime

API_KEY = "6b8475d1939bb5502208fc73e60459e5"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

class WeatherManager:
    def __init__(self, log_file="weather_log.txt"):
        self.log_file = log_file

    @retry(max_retries=3, delay=2)
    def fetch_weather(self, city):
        url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"API returned status {response.status_code}: {response.text}")
        data = response.json()

        weather = Weather(
            city=city,
            temp=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            description=data["weather"][0]["description"],
            forecast=[]
        )
        self.log_weather(weather)
        return weather

    @retry(max_retries=3, delay=2)
    def fetch_forecast(self, city):
        url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"API returned status {response.status_code}: {response.text}")
        data = response.json()

        # Extract forecast for next 3 days (daily at noon approx)
        forecast_list = []
        seen_dates = set()
        for item in data["list"]:
            dt_txt = item["dt_txt"]  # "2025-07-29 12:00:00"
            date_str = dt_txt.split()[0]
            if date_str not in seen_dates and len(forecast_list) < 3:
                forecast_list.append({
                    "date": date_str,
                    "temp": item["main"]["temp"],
                    "description": item["weather"][0]["description"]
                })
                seen_dates.add(date_str)
        return forecast_list

    def log_weather(self, weather):
        with open(self.log_file, "a") as f:
            log_line = (
                f"{datetime.now().isoformat()} | {weather.city} | "
                f"{weather.temp}°C | {weather.humidity}% | {weather.description}\n"
            )
            f.write(log_line)

    def weather_generator(self, city):
        forecast = self.fetch_forecast(city)
        if forecast:
            for day_forecast in forecast:
                yield day_forecast
