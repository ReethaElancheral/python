# 11. Recipe Finder 
# Objective: Search recipes by ingredients. 
# Requirements: 
#  OOP: Recipe class (name, ingredients, steps). 
#  List/Dict: Store recipes (key: recipe name, value: ingredients list). 
#  File Handling: Load recipes from JSON. 
#  Exception Handling: Handle missing ingredients. 
#  Functions: Search by ingredient, add new recipe. 
#  String Manipulation: Format recipe display. 
#  Loops: Filter recipes containing a given ingredient. 
#  Set: Unique ingredients across all recipes. 
#  Generator: Yield recipes one by one. 
#  Decorator: @log_search to track searches.


from recipes.core import RecipeFinder

def main():
    finder = RecipeFinder()

    while True:
        print("\n🍳 Recipe Finder Menu")
        print("1. Search recipes by ingredient")
        print("2. Add a new recipe")
        print("3. List all unique ingredients")
        print("4. List all recipes")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            ingredient = input("Enter ingredient to search for: ").strip()
            results = finder.search_by_ingredient(ingredient)
            if results:
                print(f"\nRecipes containing '{ingredient}':")
                for r in results:
                    print(r)
            else:
                print(f"No recipes found with '{ingredient}'.")

        elif choice == "2":
            name = input("Recipe name: ").strip()
            ingredients = input("Enter ingredients (comma separated): ").strip().split(',')
            ingredients = [i.strip() for i in ingredients if i.strip()]
            steps = []
            print("Enter steps (type 'done' when finished):")
            while True:
                step = input(f"Step {len(steps)+1}: ").strip()
                if step.lower() == "done":
                    break
                if step:
                    steps.append(step)
            if ingredients and steps:
                finder.add_recipe(name, ingredients, steps)
            else:
                print("⚠️ Ingredients and steps cannot be empty.")

        elif choice == "3":
            unique_ings = finder.unique_ingredients()
            print(f"\nUnique ingredients across recipes ({len(unique_ings)}):")
            print(", ".join(sorted(unique_ings)))

        elif choice == "4":
            print("\nAll Recipes:")
            for recipe in finder.recipe_generator():
                print(recipe)

        elif choice == "5":
            print("👩‍🍳 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
