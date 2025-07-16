# 9. Movie Rating System

# Description: Collect user ratings for movies.
# Requirements:
# - {movie_name: {"ratings": [int, int], "genre": ..., "avg_rating": float}}
# - Update ratings list
# - Recalculate average
# - Sort movies by avg_rating
# - Use dictionary comprehension to filter by genre


movies = {
    "Inception": {"ratings": [5, 4, 5], "genre": "Sci-Fi", "avg_rating": 0.0},
    "Titanic": {"ratings": [4, 4, 4], "genre": "Romance", "avg_rating": 0.0},
    "The Dark Knight": {"ratings": [5, 5, 5], "genre": "Action", "avg_rating": 0.0},
    "The Godfather": {"ratings": [5, 5, 5], "genre": "Crime", "avg_rating": 0.0},
}

def update_movie_rating(movie_name, new_rating):
    """Update the ratings list and recalculate the average rating."""
    if movie_name in movies:
        movies[movie_name]["ratings"].append(new_rating)
        ratings = movies[movie_name]["ratings"]
        movies[movie_name]["avg_rating"] = sum(ratings) / len(ratings)
        print(f"Updated {movie_name}: New average rating is {movies[movie_name]['avg_rating']:.2f}")
    else:
        print(f"Movie '{movie_name}' not found.")

def sort_movies_by_rating():
    """Return a list of movies sorted by average rating in descending order."""
    return sorted(movies.items(), key=lambda x: x[1]["avg_rating"], reverse=True)

def filter_movies_by_genre(genre):
    """Return a dictionary of movies filtered by genre."""
    return {name: info for name, info in movies.items() if info["genre"] == genre}


update_movie_rating("Inception", 5)
print("\nSorted Movies by Average Rating:")
for name, info in sort_movies_by_rating():
    print(f"{name}: {info['avg_rating']:.2f}")

print("\nMovies in 'Sci-Fi' Genre:")
for name, info in filter_movies_by_genre("Sci-Fi").items():
    print(f"{name}: {info['avg_rating']:.2f}")
