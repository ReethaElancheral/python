import requests

BASE_URL = "https://api.exchangerate.host"

def get_exchange_rate(base, target):
    url = f"{BASE_URL}/latest"
    params = {"base": base, "symbols": target}
    response = requests.get(url, params=params)
    data = response.json()
    if "rates" in data and target in data["rates"]:
        return data["rates"][target]
    else:
        print("Error fetching exchange rate:", data)
        return None

def get_supported_currencies():
    url = f"{BASE_URL}/symbols"
    response = requests.get(url)
    data = response.json()
    if "symbols" in data:
        return list(data["symbols"].keys())
    else:
        print("API Error:", data)
        return []

def get_historical_rates(base, target, start_date, end_date):
    url = f"{BASE_URL}/timeseries"
    params = {
        "base": base,
        "symbols": target,
        "start_date": start_date,
        "end_date": end_date,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "rates" in data:
        return data["rates"]
    else:
        print("Error fetching historical rates:", data)
        return {}
