import os
import time
from collections import defaultdict

def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\n⏱️ Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

class WordAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.word_freq = defaultdict(int)
        self.total_lines = 0
        self.total_words = 0
        self.total_chars = 0
        self.content = ""

    @time_execution
    def analyze(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("The file does not exist.")

        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.content = file.read()

        self.total_lines = self.content.count('\n') + 1
        self.total_words = len(self.content.split())
        self.total_chars = len(self.content)

        for word in self.content.lower().split():
            cleaned = ''.join(filter(str.isalnum, word))
            if cleaned:
                self.word_freq[cleaned] += 1

    def display_summary(self):
        print("\n📊 File Summary:")
        print(f"Lines     : {self.total_lines}")
        print(f"Words     : {self.total_words}")
        print(f"Characters: {self.total_chars}")

    def most_common_word(self):
        if not self.word_freq:
            return "N/A"
        return max(self.word_freq.items(), key=lambda item: item[1])

    def word_generator(self):
        for word in self.content.split():
            yield word
