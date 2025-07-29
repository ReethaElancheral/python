from textblob import TextBlob
import json
import os
from functools import lru_cache

CACHE_FILE = "sentiment_cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)

class SentimentAnalyzer:
    def __init__(self):
        self.cache = load_cache()

    def analyze_sentiment(self, text):
        if text in self.cache:
            return self.cache[text]
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        self.cache[text] = sentiment
        save_cache(self.cache)
        return sentiment

def main():
    print("Sentiment Analysis Tool (using TextBlob)")
    analyzer = SentimentAnalyzer()

    while True:
        text = input("\nEnter text to analyze (or type 'exit' to quit): ").strip()
        if text.lower() == "exit":
            break
        sentiment = analyzer.analyze_sentiment(text)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
