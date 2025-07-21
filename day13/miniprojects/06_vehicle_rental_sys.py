# 6. Vehicle Rental System

# Concepts: Inheritance, Polymorphism, Class Methods, Static Methods
# Classes:  Vehicle, Bike, Car, Rental, Customer
# Requirements:
# Rent, return vehicles
# Calculate rental charges
# Use polymorphism for calculate_rent() in each vehicle type

from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day
        self.is_rented = False

    def calculate_rent(self, days):
        """Base rent calculation, to be overridden"""
        return self.rent_per_day * days

    def __str__(self):
        status = "Rented" if self.is_rented else "Available"
        return f"{self.brand} (ID: {self.vehicle_id}) - ₹{self.rent_per_day}/day - {status}"

class Bike(Vehicle):
    def calculate_rent(self, days):
        # Bikes get 10% discount if rented for more than 3 days
        base = super().calculate_rent(days)
        if days > 3:
            return base * 0.9
        return base

class Car(Vehicle):
    def calculate_rent(self, days):
        # Cars have a fixed surcharge of ₹200 per rental
        base = super().calculate_rent(days)
        return base + 200

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"

class Rental:
    total_rentals = 0

    def __init__(self, customer, vehicle, rent_days):
        self.customer = customer
        self.vehicle = vehicle
        self.rent_days = rent_days
        self.rental_date = datetime.now()
        self.return_date = self.rental_date + timedelta(days=rent_days)
        self.vehicle.is_rented = True
        Rental.total_rentals += 1

    def return_vehicle(self):
        if self.vehicle.is_rented:
            self.vehicle.is_rented = False
            print(f"Vehicle {self.vehicle.vehicle_id} returned.")
        else:
            print("Vehicle was not rented.")

    def calculate_total_charge(self):
        return self.vehicle.calculate_rent(self.rent_days)

    @classmethod
    def get_total_rentals(cls):
        return cls.total_rentals

    @staticmethod
    def show_policy():
        print("Rental Policy: Bikes get 10% discount for rentals over 3 days. Cars have ₹200 surcharge.")

def main():
    # Create vehicles
    bike1 = Bike("B100", "Yamaha", 500)
    car1 = Car("C200", "Honda", 1500)

    # Create customer
    customer = Customer(1, "Nisha")

    # Show rental policy
    Rental.show_policy()

    # Customer rents bike for 5 days
    rental1 = Rental(customer, bike1, 5)
    print(f"{customer.name} rented {bike1} for {rental1.rent_days} days.")
    print(f"Total charge: ₹{rental1.calculate_total_charge():.2f}")

    # Customer rents car for 2 days
    rental2 = Rental(customer, car1, 2)
    print(f"{customer.name} rented {car1} for {rental2.rent_days} days.")
    print(f"Total charge: ₹{rental2.calculate_total_charge():.2f}")

    # Return vehicles
    rental1.return_vehicle()
    rental2.return_vehicle()

    print(f"Total rentals made: {Rental.get_total_rentals()}")

if __name__ == "__main__":
    main()
