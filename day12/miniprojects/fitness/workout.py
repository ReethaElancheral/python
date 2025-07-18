# fitness/workout.py

import json
from datetime import datetime

def log_workout(exercise, duration_minutes, calories_burned):
    workout = {
        'exercise': exercise,
        'duration': duration_minutes,
        'calories': calories_burned,
        'timestamp': datetime.now().isoformat()
    }
    with open('fitness/data.json', 'a') as file:
        json.dump(workout, file)
        file.write('\n')
