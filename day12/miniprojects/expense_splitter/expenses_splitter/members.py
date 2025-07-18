import csv
from decimal import Decimal
from .helper import validate_amount

def load_members(filepath):
    members = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name'].strip()
            amount = validate_amount(row['amount'])
            members.append({'name': name, 'paid': amount})
    return members
