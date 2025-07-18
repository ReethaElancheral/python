from datetime import datetime
from . import storage

def add_expense(amount, category):
    data = storage.load_data()
    data['expense'].append({
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    storage.save_data(data)

def get_total_expense():
    data = storage.load_data()
    return sum(item['amount'] for item in data['expense'])
