# 16. FrozenSet for Immutable Data

# Goal: Store fixed data in a dictionary.
# Requirements:
# - Use frozenset as dictionary keys.
# - Store meal combinations as frozen sets.
# - Retrieve data using set lookup.
# Concepts Covered: frozenset, immutability, dictionary integration.

# Define frozensets for meal combinations
breakfast = frozenset({"eggs", "toast", "coffee"})
lunch = frozenset({"salad", "sandwich", "juice"})
dinner = frozenset({"steak", "potatoes", "wine"})

# Create a dictionary with frozensets as keys
meal_plan = {
    breakfast: "Morning Boost",
    lunch: "Midday Recharge",
    dinner: "Evening Delight"
}

# Retrieve meal plan using frozenset lookup
selected_meal = frozenset({"eggs", "toast", "coffee"})
print("Meal Plan:", meal_plan.get(selected_meal, "Meal not found"))
