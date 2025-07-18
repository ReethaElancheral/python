def add_recipe(recipe_db, title, ingredients, utensils):
    recipe_key = (title.strip().lower(),)

    if recipe_key in recipe_db:
        print(f"Recipe '{title}' already exists.")
        return

    recipe_db[recipe_key] = {
        "ingredients": ingredients,
        "utensils": set(utensils)
    }

    print(f"Recipe '{title}' added successfully.")

def display_recipes(recipe_db):
    if not recipe_db:
        print("No recipes found.")
        return

    print("\n--- Recipe Book ---")
    for title_tuple, details in recipe_db.items():
        title = title_tuple[0].title()
        print(f"\nRecipe: {title}")
        print("Ingredients:")
        for item in details["ingredients"]:
            print(f" - {item}")
        print("Utensils:")
        for utensil in details["utensils"]:
            print(f" - {utensil}")
