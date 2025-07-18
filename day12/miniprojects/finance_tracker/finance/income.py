from datetime import datetime
from . import storage

def add_income(amount, source):
    data = storage.load_data()
    data['income'].append({
        "amount": amount,
        "source": source,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    storage.save_data(data)

def get_total_income():
    data = storage.load_data()
    return sum(item['amount'] for item in data['income'])
