import json
import os

FAV_FILE = "favorites.json"

def load_favorites():
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r") as f:
            return json.load(f)
    return []

def save_favorites(favorites):
    with open(FAV_FILE, "w") as f:
        json.dump(favorites, f)

def add_favorite(city):
    favorites = load_favorites()
    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)

def remove_favorite(city):
    favorites = load_favorites()
    if city in favorites:
        favorites.remove(city)
        save_favorites(favorites)
