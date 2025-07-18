# weather/cli.py
import argparse
import json
import os
from weather.api import fetch_weather
from weather.formatter import format_weather
import requests
from requests.exceptions import RequestException

API_KEY = "6b8475d1939bb5502208fc73e60459e5"; 

def save_data(data: dict):
    """Save weather data to a JSON file."""
    with open('weather_data.json', 'w') as f:
        json.dump(data, f, indent=4)

def load_data() -> dict:
    """Load weather data from a JSON file."""
    if os.path.exists('weather_data.json'):
        with open('weather_data.json', 'r') as f:
            return json.load(f)
    return {}

def main():
    parser = argparse.ArgumentParser(description="Get weather information for a city.")
    parser.add_argument('city', help="City name to get weather information for.")
    parser.add_argument('--save', action='store_true', help="Save weather data to a file.")
    parser.add_argument('--load', action='store_true', help="Load weather data from a file.")
    args = parser.parse_args()

    if args.load:
        data = load_data()
        print(json.dumps(data, indent=4))
    else:
        try:
            weather_data = fetch_weather(args.city, API_KEY)
            formatted_data = format_weather(weather_data)
            print(formatted_data)
            if args.save:
                save_data(weather_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")

if __name__ == '__main__':
    main()
