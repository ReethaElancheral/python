# converter/core.py
import requests
import json
from .utils import cache_rates
from datetime import datetime


class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.rates = self.get_rates()

    @cache_rates
    def get_rates(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()["rates"]
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return {}

    def convert(self, amount, from_currency, to_currency):
        try:
            if from_currency not in self.rates or to_currency not in self.rates:
                raise ValueError("Invalid currency code.")

            usd_amount = amount / self.rates[from_currency]
            converted = usd_amount * self.rates[to_currency]
            return round(converted, 2)
        except Exception as e:
            print(f"Conversion Error: {e}")
            return None

    def list_currencies(self):
        return sorted(self.rates.keys())

    def historical_rates(self):
        # Mock generator for last 3 days rates (as API usually needs a key)
        mock_data = {
            "2025-07-26": {"EUR": 0.91, "INR": 83.2},
            "2025-07-27": {"EUR": 0.90, "INR": 83.5},
            "2025-07-28": {"EUR": 0.89, "INR": 83.0},
        }
        for date, rates in mock_data.items():
            yield f"{date}: {rates}"
