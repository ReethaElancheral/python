# 20. Parcel Tracking System

# Concepts: Inheritance, Composition, Static/Class Methods
# Classes:  Parcel, Sender, Receiver,  Tracking
# Requirements:
# Generate tracking ID
# Use composition to link sender & receiver
# Use static method for ID validation

import random
import string

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.address}"

class Sender(Person):
    pass

class Receiver(Person):
    pass

class Tracking:
    tracking_ids = set()

    @staticmethod
    def generate_tracking_id():
        # Generate a unique 10-character alphanumeric tracking ID
        while True:
            tid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if tid not in Tracking.tracking_ids:
                Tracking.tracking_ids.add(tid)
                return tid

    @staticmethod
    def validate_tracking_id(tracking_id):
        return tracking_id in Tracking.tracking_ids

class Parcel:
    def __init__(self, sender, receiver, weight_kg):
        self.sender = sender          # composition
        self.receiver = receiver      # composition
        self.weight_kg = weight_kg
        self.tracking_id = Tracking.generate_tracking_id()

    def display_details(self):
        print(f"Parcel Tracking ID: {self.tracking_id}")
        print(f"Sender: {self.sender}")
        print(f"Receiver: {self.receiver}")
        print(f"Weight: {self.weight_kg} kg")

    def track(self):
        if Tracking.validate_tracking_id(self.tracking_id):
            print(f"Tracking ID {self.tracking_id} is valid and parcel is in transit.")
        else:
            print(f"Tracking ID {self.tracking_id} is invalid.")

def main():
    sender = Sender("Nisha", "123 Some Street, City A")
    receiver = Receiver("Ravi", "789 Another Rd, City B")
    parcel = Parcel(sender, receiver, 2.5)

    parcel.display_details()
    parcel.track()

    # Test invalid tracking ID
    print("\nTesting invalid tracking ID:")
    print(Tracking.validate_tracking_id("INVALID123"))  

if __name__ == "__main__":
    main()
