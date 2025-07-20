import random

def add_card(flashcards, categories):
    word = input("Enter word: ").strip()
    translation = input("Enter translation: ").strip()
    category = input("Enter category: ").strip()

    flashcards.append(((word, translation), category))
    categories.add(category)
    print(f"Flashcard for '{word}' added.")

def delete_card(flashcards):
    word = input("Enter word to delete: ").strip()
    for i, ((w, _), _) in enumerate(flashcards):
        if w.lower() == word.lower():
            del flashcards[i]
            print(f"Flashcard for '{word}' deleted.")
            return
    print("Flashcard not found.")

def review_cards(flashcards, stats):
    if not flashcards:
        print("No flashcards available.")
        return

    cards = flashcards.copy()
    random.shuffle(cards)

    for ((word, translation), _) in cards:
        print(f"\nTranslate: {word}")
        answer = input("Your answer: ").strip()
        if answer.lower() == translation.lower():
            print("✅ Correct!")
            stats["correct"] += 1
        else:
            print(f"❌ Incorrect. Correct answer: {translation}")
            stats["incorrect"] += 1
