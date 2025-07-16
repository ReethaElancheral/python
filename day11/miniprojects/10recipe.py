# 10. Recipe Ingredient 

# Goal: Match ingredients available at home with a recipe.
# Requirements:
# - Create a set of available ingredients.
# - Compare with required ingredients using issuperset().
# - Suggest missing items using difference().
# Concepts Covered: issuperset(), difference(), in

# Ingredients 
available = {"flour", "sugar", "eggs", "milk", "butter"}

# Ingredients needed for a recipe
required = {"flour", "milk", "eggs", "vanilla", "salt"}

# 1. Check if you're fully prepared
has_all = available.issuperset(required)

# 2. List missing ingredients
missing = required.difference(available)

# 3. Check for a specific item
has_sugar = "sugar" in available


print("Do I have all required ingredients?", has_all)
print("Missing ingredients:", missing)
print("Have sugar?", has_sugar)
