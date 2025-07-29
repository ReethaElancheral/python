def unit_converter(func):
    def wrapper(self):
        # Convert to kg if weight in lbs
        if self.unit_weight == "lb":
            self.weight = round(self.weight * 0.453592, 2)
        # Convert to meters if height in ft
        if self.unit_height == "ft":
            self.height = round(self.height * 0.3048, 2)
        return func(self)
    return wrapper
