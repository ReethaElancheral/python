import matplotlib.pyplot as plt
from .api import get_historical_rates

def show_currency_trend(base, target, start_date, end_date):
    rates = get_historical_rates(base, target, start_date, end_date)
    if not rates:
        print("No data to display.")
        return

    dates = sorted(rates.keys())
    values = [rates[date][target] for date in dates]

    plt.plot(dates, values, marker='o')
    plt.title(f"{base} to {target} Rate Trend")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()
