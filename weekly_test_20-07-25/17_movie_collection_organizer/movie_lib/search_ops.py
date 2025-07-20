def search_by_actor(movie_list, actor_name):
    result = []
    for movie in movie_list:
        if actor_name in movie["actors"]:
            result.append(movie["title"])
    return result

def search_by_genre(movie_list, genre_name):
    result = []
    for movie in movie_list:
        if genre_name in movie["genres"]:
            result.append(movie["title"])
    return result
