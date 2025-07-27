import requests

API_KEY = "6b8475d1939bb5502208fc73e60459e5"; 
BASE_URL = "https://api.openweathermap.org/data/2.5"

def get_current_weather(city):
    url = f"{BASE_URL}/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print(f"API Error: {data.get('message', 'Unknown error')}")
        return None

def get_5day_forecast(city):
    url = f"{BASE_URL}/forecast"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print(f"API Error: {data.get('message', 'Unknown error')}")
        return None
