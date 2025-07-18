# movies/search.py

from .catalog import load_from_csv

def search_by_title(query):
    return [m for m in load_from_csv() if query.lower() in m['title'].lower()]

def search_by_year(year):
    return [m for m in load_from_csv() if m['year'] == int(year)]
