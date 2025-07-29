import json
import random
from functools import wraps

def repeat(func):
    """Decorator to loop the playlist indefinitely."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        while True:
            yield from func(self, *args, **kwargs)
    return wrapper

class Playlist:
    def __init__(self):
        self.songs = []
        self.current_index = 0

    def add_song(self, song):
        if not isinstance(song, str) or not song.strip():
            raise ValueError("Invalid song name.")
        self.songs.append(song)

    def shuffle(self):
        random.shuffle(self.songs)
        self.current_index = 0

    def save_to_file(self, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.songs, f, indent=2)

    def load_from_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.songs = json.load(f)
                self.current_index = 0
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filepath}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File '{filepath}' is not a valid JSON playlist.")

    @repeat
    def next_song(self):
        if not self.songs:
            raise StopIteration("Playlist is empty.")
        while True:
            yield self.songs[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.songs)
