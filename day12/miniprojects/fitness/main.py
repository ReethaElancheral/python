# fitness/main.py

from fitness.workout import log_workout
from fitness.diet import log_diet
from fitness.progress import log_progress

def main():
    while True:
        print("Fitness Tracker")
        print("1. Log Workout")
        print("2. Log Diet")
        print("3. Log Progress")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            exercise = input("Enter exercise: ")
            duration = int(input("Enter duration in minutes: "))
            calories = int(input("Enter calories burned: "))
            log_workout(exercise, duration, calories)
        elif choice == '2':
            meal = input("Enter meal: ")
            calories = int(input("Enter calories: "))
            log_diet(meal, calories)
        elif choice == '3':
            weight = float(input("Enter weight: "))
            body_fat = float(input("Enter body fat percentage: "))
            log_progress(weight, body_fat)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
