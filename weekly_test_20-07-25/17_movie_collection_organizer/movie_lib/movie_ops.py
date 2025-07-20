def add_movie(movie_list, title, year, genres, actors):
    movie = {
        "id": (title, year),  # tuple as identifier
        "title": title,
        "year": year,
        "genres": set(genres),
        "actors": actors
    }
    movie_list.append(movie)

def group_by_genre(movie_list):
    genre_dict = {}
    for movie in movie_list:
        for genre in movie["genres"]:
            genre_dict.setdefault(genre, []).append(movie["title"])
    return genre_dict

def list_unique_genres_actors(movie_list):
    genres = set()
    actors = set()
    for movie in movie_list:
        genres.update(movie["genres"])
        actors.update(movie["actors"])
    return genres, actors
