import json
from .decorators import log_search

class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        ing_str = ', '.join(self.ingredients)
        steps_str = '\n'.join(f"{idx+1}. {step}" for idx, step in enumerate(self.steps))
        return f"Recipe: {self.name}\nIngredients: {ing_str}\nSteps:\n{steps_str}\n"

class RecipeFinder:
    def __init__(self, file_path="recipes/recipes.json"):
        self.file_path = file_path
        self.recipes = {}  # key: recipe name, value: Recipe object
        self.load_recipes()

    def load_recipes(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for name, info in data.items():
                    self.recipes[name] = Recipe(name, info["ingredients"], info["steps"])
        except FileNotFoundError:
            print("⚠️ Recipe file not found. Starting with empty collection.")
            self.recipes = {}
        except Exception as e:
            print(f"⚠️ Error loading recipes: {e}")

    @log_search
    def search_by_ingredient(self, ingredient):
        ingredient = ingredient.lower()
        found = []
        for recipe in self.recipes.values():
            if ingredient in (ing.lower() for ing in recipe.ingredients):
                found.append(recipe)
        return found

    def add_recipe(self, name, ingredients, steps):
        if name in self.recipes:
            print(f"⚠️ Recipe '{name}' already exists.")
            return
        self.recipes[name] = Recipe(name, ingredients, steps)
        self.save_recipes()
        print(f"✅ Recipe '{name}' added.")

    def save_recipes(self):
        data = {
            name: {"ingredients": r.ingredients, "steps": r.steps}
            for name, r in self.recipes.items()
        }
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def unique_ingredients(self):
        unique = set()
        for recipe in self.recipes.values():
            unique.update(ing.lower() for ing in recipe.ingredients)
        return unique

    def recipe_generator(self):
        for recipe in self.recipes.values():
            yield recipe
