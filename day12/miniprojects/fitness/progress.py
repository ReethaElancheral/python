# fitness/progress.py

import json
from datetime import datetime

def log_progress(weight, body_fat_percentage):
    progress_entry = {
        'weight': weight,
        'body_fat_percentage': body_fat_percentage,
        'timestamp': datetime.now().isoformat()
    }
    with open('fitness/data.json', 'a') as file:
        json.dump(progress_entry, file)
        file.write('\n')
