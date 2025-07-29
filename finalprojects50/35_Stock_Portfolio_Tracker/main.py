import json
import yfinance as yf
from functools import lru_cache

DATA_FILE = "portfolio.json"

def cache(func):
    """Decorator to cache API calls."""
    cache_storage = {}
    def wrapper(symbol):
        if symbol not in cache_storage:
            cache_storage[symbol] = func(symbol)
        return cache_storage[symbol]
    return wrapper

class Portfolio:
    def __init__(self):
        self.stocks = {}  # symbol: shares
        self.load()

    def load(self):
        try:
            with open(DATA_FILE, "r") as f:
                self.stocks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.stocks = {}

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.stocks, f, indent=4)

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        self.stocks[symbol] = self.stocks.get(symbol, 0) + shares
        print(f"Added {shares} shares of {symbol}.")
        self.save()

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from portfolio.")
            self.save()
        else:
            print(f"{symbol} not found in portfolio.")

    @cache
    def get_price(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            price = stock.info.get('regularMarketPrice')
            if price is None:
                raise ValueError("Price not found.")
            return price
        except Exception as e:
            print(f"Failed to fetch price for {symbol}: {e}")
            return None

    def portfolio_value(self):
        total = 0
        for sym, shares in self.stocks.items():
            price = self.get_price(sym)
            if price:
                total += price * shares
        return total

    def print_portfolio(self):
        print("\nYour Portfolio:")
        print(f"{'Symbol':<10}{'Shares':<10}{'Price':<10}{'Value':<10}")
        print("-"*40)
        for sym, shares in self.stocks.items():
            price = self.get_price(sym)
            val = price * shares if price else 0
            price_str = f"{price:.2f}" if price else "N/A"
            val_str = f"{val:.2f}" if price else "N/A"
            print(f"{sym:<10}{shares:<10}{price_str:<10}{val_str:<10}")
        print("-"*40)
        print(f"Total Portfolio Value: ₹{self.portfolio_value():.2f}")

def main():
    portfolio = Portfolio()

    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            symbol = input("Enter stock symbol: ").strip()
            try:
                shares = int(input("Enter number of shares: "))
                if shares <= 0:
                    raise ValueError
                portfolio.add_stock(symbol, shares)
            except ValueError:
                print("Invalid number of shares.")
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").strip()
            portfolio.remove_stock(symbol)
        elif choice == '3':
            portfolio.print_portfolio()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

