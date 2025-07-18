from recipes.recipe_book import add_recipe, display_recipes

def main():
    recipe_db = {}

    while True:
        print("\n=== Recipe Manager ===")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter recipe title: ")

            try:
                n = int(input("How many ingredients? "))
                ingredients = [input(f"Ingredient #{i+1}: ") for i in range(n)]

                m = int(input("How many utensils? "))
                utensils = {input(f"Utensil #{i+1}: ") for i in range(m)}
            except ValueError:
                print("Invalid input.")
                continue

            add_recipe(recipe_db, title, ingredients, utensils)

        elif choice == '2':
            display_recipes(recipe_db)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
