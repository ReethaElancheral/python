# ✅ 15. Temperature Category Classifier

# Objective: Classify temperatures as Cold/Warm/Hot.
# Requirements:
# Input: list of temperatures.
# Use for loop + if to print category for each:
# <20: Cold, 20–30: Warm, >30: Hot

temps_input = input("Enter temperatures in celcius separated by commas: ").split(',')

temperatures = [float(temp.strip()) for temp in temps_input]

print("\nTemperature Categories:")
for temp in temperatures:
    if temp < 20:
        category = "Cold"
    elif 20 <= temp <= 30:
        category = "Warm"
    else:
        category = "Hot"
    print(f"{temp}°C → {category}")
