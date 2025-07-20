from recipe_io import (
    load_recipes,
    save_recipes,
    search_by_ingredient,
    add_recipe,
    remove_recipe,
    modify_recipe
)

def show_all(recipes):
    print("\n--- All Recipes ---")
    for name in sorted(recipes.keys()):
        print(f"\n{name}")
        print("Ingredients:", ", ".join(recipes[name]["ingredients"]))
        print("Steps:", " -> ".join(recipes[name]["steps"]))

def main():
    recipes = load_recipes()
    while True:
        print("\nRecipe Book Menu:")
        print("1. Show All Recipes")
        print("2. Search by Ingredient")
        print("3. Add Recipe")
        print("4. Remove Recipe")
        print("5. Modify Recipe")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all(recipes)
        elif choice == "2":
            ing = input("Enter ingredient to search: ")
            result = search_by_ingredient(recipes, ing)
            if result:
                show_all(result)
            else:
                print("No recipes found with that ingredient.")
        elif choice == "3":
            name = input("Recipe name: ")
            ingredients = input("Ingredients (comma-separated): ").split(",")
            steps = input("Steps (comma-separated): ").split(",")
            add_recipe(recipes, name, [i.strip() for i in ingredients], [s.strip() for s in steps])
            print(f"{name} added.")
        elif choice == "4":
            name = input("Recipe name to remove: ")
            remove_recipe(recipes, name)
            print(f"{name} removed.")
        elif choice == "5":
            name = input("Recipe name to modify: ")
            if name not in recipes:
                print("Recipe not found.")
                continue
            new_ing = input("New ingredients (comma-separated, leave blank to skip): ")
            new_steps = input("New steps (comma-separated, leave blank to skip): ")
            modify_recipe(
                recipes,
                name,
                [i.strip() for i in new_ing.split(",")] if new_ing else None,
                [s.strip() for s in new_steps.split(",")] if new_steps else None
            )
            print(f"{name} updated.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
