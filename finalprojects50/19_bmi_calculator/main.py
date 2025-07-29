# 19. BMI Calculator 
# Objective: Calculate BMI and classify health risk. 
# Requirements: 
#  OOP: Person class (weight, height). 
#  File Handling: Save BMI history. 
#  Exception Handling: Negative weight/height. 
#  Functions: Compute BMI, classify (Underweight/Normal/Overweight). 
#  Conditionals: Health risk based on BMI. 
#  Loops: Track multiple people. 
#  Generator: Yield people in "Obese" category. 
#  Decorator: @unit_converter (kg/lb, cm/ft).



from bmi.core import Person, BMITracker

def main():
    print("🧮 BMI Calculator & Health Classifier")
    tracker = BMITracker()

    while True:
        try:
            name = input("\nEnter name: ")
            weight = float(input("Enter weight: "))
            unit_w = input("Unit of weight (kg/lb): ").strip()

            height = float(input("Enter height: "))
            unit_h = input("Unit of height (m/ft): ").strip()

            person = Person(name, weight, height, unit_w, unit_h)
            tracker.add_person(person)

            print(f"\n✅ {name}'s BMI is {person.bmi} ({person.status}) - Risk: {person.risk}")

        except ValueError as e:
            print(f"⚠️ Error: {e}")

        more = input("\nAdd another person? (y/n): ").lower()
        if more != 'y':
            break

    print("\n🚨 People in Obese category:")
    for p in tracker.show_obese():
        print(f" - {p.name}: BMI {p.bmi} ({p.status})")

if __name__ == "__main__":
    main()
