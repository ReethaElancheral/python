# 5. Hospital Management System

# Concepts: Class, Multilevel Inheritance, Aggregation, Abstraction
# Classes:  Person, Doctor, Patient, Appointment,  Prescription
# Requirements:
# Book appointments, assign doctors
# Generate prescriptions
# Use abstract class Person
# Use method overriding for role-based access

from abc import ABC, abstractmethod
from datetime import datetime


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.get_role()}: {self.name}, Age: {self.age}"

# Doctor inherits Person
class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty
        self.patients = []  # Aggregation: doctors have patients

    def get_role(self):
        return "Doctor"

    def assign_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} assigned to Dr. {self.name}")

# Patient inherits Person
class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.appointments = []  # Aggregation: patient has appointments
        self.prescriptions = []

    def get_role(self):
        return "Patient"

    def book_appointment(self, doctor, date_time):
        appt = Appointment(self, doctor, date_time)
        self.appointments.append(appt)
        doctor.assign_patient(self)
        print(f"Appointment booked on {date_time} with Dr. {doctor.name}")
        return appt

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)
        print(f"Prescription added for patient {self.name}")

# Appointment class aggregates Patient and Doctor
class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        return f"Appointment: {self.date_time} with Dr. {self.doctor.name} for {self.patient.name}"

# Prescription class
class Prescription:
    def __init__(self, patient, doctor, medicines):
        self.patient = patient
        self.doctor = doctor
        self.medicines = medicines
        self.date = datetime.now()

    def __str__(self):
        meds = ", ".join(self.medicines)
        return (f"Prescription for {self.patient.name} by Dr. {self.doctor.name} on "
                f"{self.date.strftime('%Y-%m-%d')}:\nMedicines: {meds}")


def main():

    doctor = Doctor("Dr. Asha", 45, "Cardiology")
    patient = Patient("Nisha", 30, "P1001")

    # Patient books appointment
    appointment = patient.book_appointment(doctor, "2025-08-01 10:00 AM")
    print(appointment)

    # Doctor generates prescription
    prescription = Prescription(patient, doctor, ["Aspirin", "Atorvastatin"])
    patient.add_prescription(prescription)

    # Display prescription
    print(prescription)

    # Show patient details and prescriptions
    print(patient)
    for p in patient.prescriptions:
        print(p)

if __name__ == "__main__":
    main()
