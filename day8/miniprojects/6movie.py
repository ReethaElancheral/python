# 6. Movie Watchlist App

# Description: Users can manage a list of movies to watch.
# Add movies to the list.
# Mark as watched (remove).
# Show top 5 movies to watch using slicing.
# Print with index using a loop.


watchlist = []

def show_watchlist():
    if not watchlist:
        print("🎉 Your watchlist is empty!")
    else:
        print("\n🎬 Movies in your Watchlist:")
        for index, movie in enumerate(watchlist, 1):
            print(f"{index}. {movie}")

def add_movie():
    movie = input("Enter movie name to add: ").strip()
    if movie:
        watchlist.append(movie)
        print(f"✅ '{movie}' added to your watchlist.")
    else:
        print("❌ Movie name cannot be empty.")

def mark_watched():
    show_watchlist()
    if not watchlist:
        return
    try:
        index = int(input("Enter the number of the movie you watched: ")) - 1
        if 0 <= index < len(watchlist):
            watched = watchlist.pop(index)
            print(f"✅ '{watched}' marked as watched and removed.")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def show_top5():
    print("\n🎯 Top 5 Movies To Watch:")
    top_movies = watchlist[:5]
    if top_movies:
        for i, movie in enumerate(top_movies, 1):
            print(f"{i}. {movie}")
    else:
        print("No movies in your list.")


while True:
    print("\n--- Movie Watchlist Menu ---")
    print("1. View Watchlist")
    print("2. Add Movie")
    print("3. Mark Movie as Watched")
    print("4. Show Top 5 Movies")
    print("5. Exit")

    choice = input("Choose an option (1–5): ")

    if choice == "1":
        show_watchlist()
    elif choice == "2":
        add_movie()
    elif choice == "3":
        mark_watched()
    elif choice == "4":
        show_top5()
    elif choice == "5":
        print("🎬 Goodbye! Enjoy your movies!")
        break
    else:
        print("❌ Invalid choice. Enter a number between 1–5.")
