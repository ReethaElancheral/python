import json
import random
import string
import time
from urllib.parse import urlparse

class InvalidURLException(Exception):
    pass

class URLShortener:
    def __init__(self, data_file="urlshortener/data.json"):
        self.data_file = data_file
        self.url_map = {}  # short_code -> {original_url, created_time, access_count}
        self.load_mappings()

    def load_mappings(self):
        try:
            with open(self.data_file, "r") as f:
                self.url_map = json.load(f)
        except FileNotFoundError:
            self.url_map = {}

    def save_mappings(self):
        with open(self.data_file, "w") as f:
            json.dump(self.url_map, f, indent=2)

    def validate_url(self, url):
        parsed = urlparse(url)
        if not (parsed.scheme and parsed.netloc):
            raise InvalidURLException("Invalid URL format.")

    def generate_short_code(self, length=6):
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choice(chars) for _ in range(length))
            if code not in self.url_map:
                return code

    def shorten_url(self, original_url):
        self.validate_url(original_url)
        # Check if URL already shortened
        for code, data in self.url_map.items():
            if data["original_url"] == original_url:
                return code

        code = self.generate_short_code()
        self.url_map[code] = {
            "original_url": original_url,
            "created_time": time.time(),
            "access_count": 0
        }
        self.save_mappings()
        return code

    from urlshortener.decorators import cache


    @cache
    def redirect(self, short_code):
        if short_code not in self.url_map:
            print("❌ Short code not found.")
            return None
        self.url_map[short_code]["access_count"] += 1
        self.save_mappings()
        return self.url_map[short_code]["original_url"]


    def delete_url(self, short_code):
        if short_code in self.url_map:
            del self.url_map[short_code]
            self.save_mappings()
            print(f"✅ Short URL '{short_code}' deleted.")
        else:
            print("❌ Short code not found.")

    def list_urls(self):
        if not self.url_map:
            print("No URLs shortened yet.")
            return
        for code, data in self.url_map.items():
            print(f"{code} -> {data['original_url']} (Accessed {data['access_count']} times)")

    def expired_urls_generator(self, expiry_seconds=60*60*24*7):
        # Yield URLs older than expiry_seconds (default 7 days)
        current_time = time.time()
        for code, data in self.url_map.items():
            if (current_time - data["created_time"]) > expiry_seconds:
                yield code, data["original_url"]
