import feedparser
import json
import os
from datetime import datetime

CACHE_FILE = "rss_cache.json"

class Feed:
    def __init__(self, url):
        self.url = url
        self.articles = []
        self.load_cache()

    def load_cache(self):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                self.cache = json.load(f)
        else:
            self.cache = {}

    def save_cache(self):
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, indent=4)

    def fetch(self):
        feed = feedparser.parse(self.url)
        new_items = []
        for entry in feed.entries:
            # Use link as unique id
            if entry.link not in self.cache:
                article = {
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", ""),
                }
                self.articles.append(article)
                self.cache[entry.link] = datetime.now().isoformat()
                new_items.append(article)
        self.save_cache()
        return new_items

def main():
    print("RSS Feed Reader")
    url = input("Enter RSS feed URL: ").strip()
    feed = Feed(url)

    new_articles = feed.fetch()
    if not new_articles:
        print("No new articles found.")
    else:
        print(f"\nNew articles ({len(new_articles)}):")
        for i, article in enumerate(new_articles, 1):
            print(f"\n[{i}] {article['title']}")
            print(f"Link: {article['link']}")
            print(f"Published: {article['published']}")
            print(f"Summary: {article['summary'][:200]}...")  # Show first 200 chars

if __name__ == "__main__":
    main()
