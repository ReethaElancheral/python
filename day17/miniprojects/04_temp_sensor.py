# 4. Temperature Sensor Stream 

# Objective: Simulate a real-time sensor stream using generators. 
# Requirements: 
#  Use infinite generator with random temperature values. 
#  Break on reading above 100. 
#  Use iter(callable, sentinel) for lazy stream. 
#  send() used to manually inject "override" values. 

import random

def temp_sensor():
    while True:
        temp = random.randint(20, 110)
        override = (yield temp)
        if override is not None:
            yield override
        if temp > 100:
            break

sensor = temp_sensor()
print("Temperature Sensor Stream:")
for _ in range(10):
    try:
        reading = next(sensor)
        print(f"Reading: {reading}°C")
        if reading > 100:
            print("High temperature! Stopping sensor.")
            break
    except StopIteration:
        break
