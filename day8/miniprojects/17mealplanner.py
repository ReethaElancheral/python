# 17. Daily Meal Planner

# Description: Store meal plans for a week.
# Use a nested list: [[“Monday”, “Idly”], …].
# Update meals.
# Remove meals.
# Slice to view weekend plans.


meal_plan = [
    ["Monday", "Idly"],
    ["Tuesday", "Dosa"],
    ["Wednesday", "Chapati"],
    ["Thursday", "Rice"],
    ["Friday", "Biriyani"],
    ["Saturday", "Pasta"],
    ["Sunday", "Pizza"]
]

def show_meals():
    print("\n🍴 Weekly Meal Plan:")
    for day, meal in meal_plan:
        print(f"{day}: {meal}")

def update_meal():
    day = input("Enter day to update meal: ").capitalize()
    for i, (d, m) in enumerate(meal_plan):
        if d == day:
            new_meal = input(f"Enter new meal for {day}: ").strip()
            meal_plan[i][1] = new_meal
            print(f"{day} meal updated to {new_meal}.")
            return
    print("Day not found in meal plan.")

def remove_meal():
    day = input("Enter day to remove meal from: ").capitalize()
    for i, (d, m) in enumerate(meal_plan):
        if d == day:
            meal_plan.pop(i)
            print(f"{day} meal removed from plan.")
            return
    print("Day not found in meal plan.")

def show_weekend():
   
    weekend = [item for item in meal_plan if item[0] in ["Saturday", "Sunday"]]
    if weekend:
        print("\n🌞 Weekend Meal Plan:")
        for day, meal in weekend:
            print(f"{day}: {meal}")
    else:
        print("No weekend meals found.")


while True:
    print("\n--- Daily Meal Planner ---")
    print("1. Show Meal Plan")
    print("2. Update Meal")
    print("3. Remove Meal")
    print("4. Show Weekend Meals")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_meals()
    elif choice == "2":
        update_meal()
    elif choice == "3":
        remove_meal()
    elif choice == "4":
        show_weekend()
    elif choice == "5":
        print("Exiting Meal Planner. Bon appétit!")
        break
    else:
        print("Invalid choice.")
