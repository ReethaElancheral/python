# 6. Lazy Dictionary Translator 

# Objective: Translate words from English to Tamil lazily using generator. 
# Requirements: 
#  Use generator expression to lazily translate a list of words. 
#  Support filtering for unknown words. 
#  Use chaining: yield word, yield translated word.

from typing import Generator

# Sample English to Tamil dictionary
dictionary = {
    "hello": "வணக்கம்",
    "world": "உலகம்",
    "love": "காதல்",
    "friend": "நண்பர்",
    "good": "நல்ல",
    "food": "உணவு",
    "night": "இரவு",
    "day": "நாள்"
}

def lazy_translator(words: list) -> Generator[str, None, None]:
    for word in words:
        yield word  # yield original word
        translated = dictionary.get(word.lower())
        if translated:
            yield translated
        else:
            yield "[Unknown]"

# Sample word list 
word_list = ["Hello", "world", "cat", "Love", "dog", "Food"]

# Using the generator
print("Lazy Dictionary Translator:")
for output in lazy_translator(word_list):
    print(output)
