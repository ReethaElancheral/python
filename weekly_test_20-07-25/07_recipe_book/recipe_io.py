import json
import os

RECIPE_FILE = "recipes.json"

def load_recipes():
    if not os.path.exists(RECIPE_FILE):
        return {}
    with open(RECIPE_FILE, "r") as file:
        return json.load(file)

def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as file:
        json.dump(recipes, file, indent=2)

def search_by_ingredient(recipes, ingredient):
    result = {}
    for name, details in recipes.items():
        if ingredient.lower() in [i.lower() for i in details['ingredients']]:
            result[name] = details
    return result

def add_recipe(recipes, name, ingredients, steps):
    recipes[name] = {
        "ingredients": ingredients,
        "steps": steps
    }
    save_recipes(recipes)

def remove_recipe(recipes, name):
    if name in recipes:
        del recipes[name]
        save_recipes(recipes)

def modify_recipe(recipes, name, ingredients=None, steps=None):
    if name in recipes:
        if ingredients is not None:
            recipes[name]["ingredients"] = ingredients
        if steps is not None:
            recipes[name]["steps"] = steps
        save_recipes(recipes)
