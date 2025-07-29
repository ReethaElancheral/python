import random

from .decorators import validate_input

class Hangman:
    def __init__(self, words_file="hangman/words.txt", max_attempts=6):
        self.words_file = words_file
        self.max_attempts = max_attempts
        self.word = self.load_word().lower()
        self.attempts_left = max_attempts
        self.guessed_letters = []
        self.failed_attempts = 0

    def load_word(self):
        try:
            with open(self.words_file, 'r') as f:
                words = [line.strip() for line in f if line.strip()]
                if not words:
                    raise ValueError("Word list is empty!")
                return random.choice(words)
        except FileNotFoundError:
            print("⚠️ Words file not found. Using default word 'python'.")
            return "python"

    def display_word(self):
        displayed = ' '.join([c if c in self.guessed_letters else '_' for c in self.word])
        print(f"Word: {displayed}")

    @validate_input
    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print(f"⚠️ You've already guessed '{letter}'. Try another letter.")
            return False

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.attempts_left -= 1
            self.failed_attempts += 1
            print(f"❌ Wrong guess! Attempts left: {self.attempts_left}")
            return False
        else:
            print("✅ Good guess!")
            return True

    def is_won(self):
        return all(c in self.guessed_letters for c in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

    def hint_generator(self):
        # Yield one hint (letter from word) after 3 failed attempts and every subsequent failed attempt
        hints_given = set()
        while self.failed_attempts >= 3:
            for letter in self.word:
                if letter not in self.guessed_letters and letter not in hints_given:
                    hints_given.add(letter)
                    yield f"Hint: The word contains letter '{letter}'"
            return  # Yield hints once per fail threshold only
