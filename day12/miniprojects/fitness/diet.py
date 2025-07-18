# fitness/diet.py

import json
from datetime import datetime

def log_diet(meal, calories):
    diet_entry = {
        'meal': meal,
        'calories': calories,
        'timestamp': datetime.now().isoformat()
    }
    with open('fitness/data.json', 'a') as file:
        json.dump(diet_entry, file)
        file.write('\n')
