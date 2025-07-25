# 6. Sensor Alert System 

# Goal: Use iter(callable, sentinel) to simulate reading sensor values until a critical 
# value is reached. 
# Requirements: 
#  Generate random values until 99 
#  Use iter() with a function 
#  Raise alert when sentinel reached 


import random

def sensor_read():
    val = random.randint(80, 100)
    print(f"Sensor reading: {val}")
    return val

print("Sensor readings until critical value (99) reached:")
try:
    for reading in iter(sensor_read, 99):
        pass
    print("Alert! Critical value reached: 99")
except Exception as e:
    print("Error:", e)
