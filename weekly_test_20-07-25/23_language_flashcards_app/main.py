import random
from flashcards.card_ops import add_card, delete_card, review_cards
from flashcards.stats import show_stats

def main():
    flashcards = []
    categories = set()
    stats = {"correct": 0, "incorrect": 0}

    while True:
        print("\n=== Language Flashcards App ===")
        print("1. Add Flashcard")
        print("2. Delete Flashcard")
        print("3. Review (Quiz Mode)")
        print("4. Show Stats")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_card(flashcards, categories)
        elif choice == "2":
            delete_card(flashcards)
        elif choice == "3":
            review_cards(flashcards, stats)
        elif choice == "4":
            show_stats(stats)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
