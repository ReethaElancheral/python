# movies/catalog.py

import csv
import pickle
from datetime import datetime
from pathlib import Path

DATA_CSV = Path(__file__).parent / "data" / "movies.csv"
DATA_PKL = Path(__file__).parent / "data" / "movies.pkl"

def load_from_csv():
    movies = []
    if not DATA_CSV.exists():
        return movies
    with open(DATA_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['added'] = datetime.fromisoformat(row['added'])
            row['rating'] = float(row['rating'])
            movies.append(row)
    return movies

def save_to_csv(movies):
    with open(DATA_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title','year','rating','added'])
        writer.writeheader()
        for m in movies:
            writer.writerow({
                'title': m['title'],
                'year': m['year'],
                'rating': m['rating'],
                'added': m['added'].isoformat()
            })

def load_from_pickle():
    if not DATA_PKL.exists():
        return []
    with open(DATA_PKL, 'rb') as f:
        return pickle.load(f)

def save_to_pickle(movies):
    with open(DATA_PKL, 'wb') as f:
        pickle.dump(movies, f, protocol=pickle.HIGHEST_PROTOCOL)
