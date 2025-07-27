def convert_length(value, from_unit, to_unit):
    units = {"m": 1, "cm": 100, "mm": 1000, "km": 0.001}
    if from_unit in units and to_unit in units:
        return value * units[to_unit] / units[from_unit]
    return "Invalid units"

def convert_weight(value, from_unit, to_unit):
    units = {"kg": 1, "g": 1000, "mg": 1e6}
    if from_unit in units and to_unit in units:
        return value * units[to_unit] / units[from_unit]
    return "Invalid units"
