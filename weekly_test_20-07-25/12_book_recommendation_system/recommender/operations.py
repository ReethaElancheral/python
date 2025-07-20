import random

def search_books(books, author_name):
    return [book for book in books if book["author"] == author_name]

def recommend_books(books, target_genres):
    recommendations = []
    for book in books:
        if book["genres"] & target_genres:
            recommendations.append(book)
    random.shuffle(recommendations)
    return recommendations
