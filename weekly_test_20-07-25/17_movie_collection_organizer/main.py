from movie_lib.movie_ops import add_movie, group_by_genre, list_unique_genres_actors
from movie_lib.search_ops import search_by_actor, search_by_genre

if __name__ == "__main__":
    movies = []

    
    add_movie(movies, "Inception", 2010, {"Sci-Fi", "Thriller"}, ["Leonardo DiCaprio", "Tom Hardy"])
    add_movie(movies, "The Dark Knight", 2008, {"Action", "Drama"}, ["Christian Bale", "Heath Ledger"])
    add_movie(movies, "Titanic", 1997, {"Romance", "Drama"}, ["Leonardo DiCaprio", "Kate Winslet"])

    # Display grouped by genre
    grouped = group_by_genre(movies)
    print("\n🎬 Movies Grouped by Genre:")
    for genre, titles in grouped.items():
        print(f"- {genre}: {titles}")

    # Unique genres and actors
    genres, actors = list_unique_genres_actors(movies)
    print(f"\n✅ Unique Genres: {genres}")
    print(f"✅ Unique Actors: {actors}")

    # Search examples
    print("\n🔍 Search Results:")
    print("By Actor 'Leonardo DiCaprio':", search_by_actor(movies, "Leonardo DiCaprio"))
    print("By Genre 'Drama':", search_by_genre(movies, "Drama"))
