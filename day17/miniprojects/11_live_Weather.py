# 11. Live Weather Notifier 

# Objective: Create a generator-based system that fetches and lazily evaluates 
# temperature change. 
# Requirements: 
#  Simulate API results with random values. 
#  Use generator expression to yield only significant changes (±5°). 
#  Add infinite loop logic with exit condition.

import random
import time

def live_weather_notifier():
    prev_temp = random.randint(20, 30)
    while True:
        time.sleep(1)  # simulate delay
        new_temp = random.randint(20, 40)
        diff = abs(new_temp - prev_temp)
        if diff >= 5:
            yield f"Significant temperature change: {prev_temp}°C → {new_temp}°C"
        prev_temp = new_temp

# Example usage (stop after 5 changes)
notifier = live_weather_notifier()
for i in range(5):
    print(next(notifier))
