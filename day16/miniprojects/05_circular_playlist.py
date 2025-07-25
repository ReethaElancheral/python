# 5. Circular Playlist Navigator 

# Goal: Implement a playlist where songs cycle indefinitely using an infinite iterator. 
# Requirements: 
#  Class-based iterator 
#  Loops back after the last song 
#  Stop manually after 10 iterations using break


class CircularPlaylist:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        song = self.songs[self.index]
        self.index = (self.index + 1) % len(self.songs)
        return song

# Usage & Output
playlist = CircularPlaylist(["Song A", "Song B", "Song C"])
print("Circular Playlist (first 10 songs):")
it = iter(playlist)
for _ in range(10):
    print(next(it))
