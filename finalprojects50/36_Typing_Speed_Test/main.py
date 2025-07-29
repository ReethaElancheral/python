import time
import random
import json
import os
from functools import wraps

HISTORY_FILE = "typing_history.json"

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"\nTime taken: {duration:.2f} seconds")
        return result, duration
    return wrapper

class TypingTest:
    def __init__(self):
        self.samples = [
            "The quick brown fox jumps over the lazy dog",
            "Practice makes perfect",
            "Typing speed is important for programmers",
            "Python is a great programming language",
            "Never stop learning new things",
            "OpenAI creates powerful AI models",
            "Consistency is the key to success",
            "Focus and determination bring results"
        ]
        self.results = []
        self.load_history()

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r") as f:
                    self.results = json.load(f)
            except Exception:
                self.results = []

    def save_history(self):
        with open(HISTORY_FILE, "w") as f:
            json.dump(self.results, f, indent=4)

    @timed
    def run_test(self, text):
        print("\nType the following sentence:")
        print(f">>> {text}\n")
        input_text = input("Start typing:\n")
        return input_text

    def calculate_accuracy(self, original, typed):
        original_words = original.split()
        typed_words = typed.split()
        correct = sum(o == t for o, t in zip(original_words, typed_words))
        accuracy = (correct / len(original_words)) * 100
        return accuracy

    def print_results(self):
        print("\n--- Typing Test Results ---")
        for i, r in enumerate(self.results[-5:], 1):  # last 5 results
            print(f"{i}. Time: {r['time']:.2f}s | Accuracy: {r['accuracy']:.2f}% | Text: {r['text']}")

    def generator(self):
        for sample in self.samples:
            yield sample

def main():
    test = TypingTest()
    gen = test.generator()

    while True:
        try:
            sample_text = next(gen)
        except StopIteration:
            print("No more samples! Restarting...")
            gen = test.generator()
            sample_text = next(gen)

        typed_text, duration = test.run_test(sample_text)
        accuracy = test.calculate_accuracy(sample_text, typed_text)
        print(f"Accuracy: {accuracy:.2f}%")

        test.results.append({
            "text": sample_text,
            "time": duration,
            "accuracy": accuracy
        })
        test.save_history()

        test.print_results()

        cont = input("\nDo another test? (y/n): ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()

