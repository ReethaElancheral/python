# converter/temperature/fahrenheit.py

import math

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
