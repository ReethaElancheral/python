import csv
from .decorators import unit_converter

class Person:
    def __init__(self, name, weight, height, unit_weight="kg", unit_height="m"):
        if weight <= 0 or height <= 0:
            raise ValueError("❌ Weight and height must be positive numbers.")
        self.name = name
        self.weight = weight
        self.height = height
        self.unit_weight = unit_weight.lower()
        self.unit_height = unit_height.lower()
        self.bmi = 0
        self.status = ""
        self.risk = ""

    @unit_converter
    def calculate_bmi(self):
        self.bmi = round(self.weight / (self.height ** 2), 2)
        self.classify()
        return self.bmi

    def classify(self):
        bmi = self.bmi
        if bmi < 18.5:
            self.status = "Underweight"
            self.risk = "Low"
        elif 18.5 <= bmi < 24.9:
            self.status = "Normal"
            self.risk = "Average"
        elif 25 <= bmi < 29.9:
            self.status = "Overweight"
            self.risk = "Elevated"
        else:
            self.status = "Obese"
            self.risk = "High"

    def get_details(self):
        return {
            "Name": self.name,
            "Weight (kg)": self.weight,
            "Height (m)": self.height,
            "BMI": self.bmi,
            "Status": self.status,
            "Health Risk": self.risk
        }

class BMITracker:
    def __init__(self):
        self.people = []

    def add_person(self, person: Person):
        bmi = person.calculate_bmi()
        self.people.append(person)
        self.save_to_csv(person)

    def save_to_csv(self, person):
        with open("bmi_history.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=person.get_details().keys())
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(person.get_details())

    def show_obese(self):
        for person in self.people:
            if person.status == "Obese":
                yield person
