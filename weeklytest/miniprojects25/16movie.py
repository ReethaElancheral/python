# 16. Movie Rating Collector

# Concepts: list, while, strings, functions.
# Collect movie names and user ratings.
# Store in nested lists.
# Show top-rated movies.

movies = []  

def add_movie():
    name = input("Enter movie name: ").strip()
    rating = input("Enter your rating (0-10): ").strip()
    
    if not name:
        print("Movie name cannot be empty.")
        return

    if rating.replace('.', '', 1).isdigit():
        rating = float(rating)
        if 0 <= rating <= 10:
            movies.append([name, rating])
            print(f"Added '{name}' with rating {rating:.1f}")
        else:
            print("Rating must be between 0 and 10.")
    else:
        print("Invalid rating. Enter a number between 0 and 10.")

def show_movies():
    if not movies:
        print("No movies added yet.")
        return
    print("\nAll Movies and Ratings:")
    for i, (name, rating) in enumerate(movies, 1):
        print(f"{i}. {name} - Rating: {rating:.1f}")
    print()

def show_top_rated():
    if not movies:
        print("No movies added yet.")
        return
    max_rating = max(m[1] for m in movies)
    top_movies = [m for m in movies if m[1] == max_rating]

    print(f"\nTop Rated Movie(s) with rating {max_rating:.1f}:")
    for name, rating in top_movies:
        print(f"- {name}")


while True:
    print("\n=== Movie Rating Collector ===")
    print("1. Add Movie and Rating")
    print("2. Show All Movies")
    print("3. Show Top Rated Movie(s)")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        add_movie()
    elif choice == "2":
        show_movies()
    elif choice == "3":
        show_top_rated()
    elif choice == "4":
        print("Exiting Movie Rating Collector. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 4.")
