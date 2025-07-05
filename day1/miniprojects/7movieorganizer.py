## 7. Movie Organizer
# - Ask the user for three favorite movies.
# - Store them in a tuple.
# - Print the entire tuple and each movie separately.
# - Display the type using type().

movie1 = input("Enter your first favorite movie: ")
movie2 = input("Enter your second favorite movie: ")
movie3 = input("Enter your third favorite movie: ")

fav_movies = (movie1, movie2, movie3)
print("Your favorite movies are:", fav_movies)

print("Movie 1:", fav_movies[0])
print("Movie 2:", fav_movies[1])
print("Movie 3:", fav_movies[2])


print("Type of favorite_movies:", type(fav_movies))