# movies/ratings.py

from .catalog import load_from_csv, save_to_csv

def update_rating(title, rating):
    movies = load_from_csv()
    found = False
    for m in movies:
        if m['title'].lower() == title.lower():
            m['rating'] = float(rating)
            found = True
            break
    if not found:
        return False
    save_to_csv(movies)
    return True
