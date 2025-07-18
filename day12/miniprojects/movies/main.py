# movies/main.py

import argparse
from datetime import datetime
from .catalog import (load_from_csv, save_to_csv, load_from_pickle, save_to_pickle)
from .ratings import update_rating
from .search import search_by_title, search_by_year

def add_movie(title, year, rating):
    movies = load_from_csv()
    movies.append({
        'title': title,
        'year': int(year),
        'rating': float(rating),
        'added': datetime.now()
    })
    save_to_csv(movies)
    save_to_pickle(movies)
    print(f"Movie added: {title} ({year})")

def list_movies():
    movies = load_from_csv()
    for m in movies:
        a = m['added'].strftime("%Y-%m-%d")
        print(f"{m['title']} – {m['year']} – rating: {m['rating']} – added: {a}")

def main():
    p = argparse.ArgumentParser("Movie Manager")
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser("add")
    a.add_argument("title")
    a.add_argument("year", type=int)
    a.add_argument("rating", type=float)

    u = sub.add_parser("rate")
    u.add_argument("title")
    u.add_argument("rating", type=float)

    st = sub.add_parser("search-title")
    st.add_argument("query")

    sy = sub.add_parser("search-year")
    sy.add_argument("year", type=int)

    l = sub.add_parser("list")

    args = p.parse_args()

    if args.cmd == "add":
        add_movie(args.title, args.year, args.rating)
    elif args.cmd == "rate":
        if update_rating(args.title, args.rating):
            print("Rating updated.")
        else:
            print("Movie not found.")
    elif args.cmd == "search-title":
        for m in search_by_title(args.query):
            print(f"{m['title']} ({m['year']}) — Rating: {m['rating']}")
    elif args.cmd == "search-year":
        for m in search_by_year(args.year):
            print(f"{m['title']} — Rating: {m['rating']}")
    elif args.cmd == "list":
        list_movies()
    else:
        p.print_help()

if __name__ == "__main__":
    main()
