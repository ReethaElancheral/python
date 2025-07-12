# 16. Music Playlist Creator

# Description: Build a playlist using list operations.
# Add songs, remove songs.
# Display all songs.
# Repeat songs using * repetition.
# Search using in.



playlist = []

def show_playlist():
    if not playlist:
        print("Your playlist is empty.")
    else:
        print("\n🎶 Your Playlist:")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song}")

def add_song():
    song = input("Enter song name to add: ").strip()
    if song:
        playlist.append(song)
        print(f"'{song}' added to your playlist.")
    else:
        print("Song name cannot be empty.")

def remove_song():
    song = input("Enter song name to remove: ").strip()
    if song in playlist:
        playlist.remove(song)
        print(f"'{song}' removed from your playlist.")
    else:
        print(f"'{song}' is not in your playlist.")

def repeat_playlist():
    times = input("How many times to repeat the playlist? ")
    if times.isdigit():
        times = int(times)
        repeated = playlist * times
        print(f"\n🎧 Playlist repeated {times} times:")
        for i, song in enumerate(repeated, 1):
            print(f"{i}. {song}")
    else:
        print("Please enter a valid number.")

def search_song():
    song = input("Enter song name to search: ").strip()
    if song in playlist:
        print(f"'{song}' is in your playlist.")
    else:
        print(f"'{song}' is not in your playlist.")

while True:
    print("\n--- Music Playlist Creator ---")
    print("1. Show Playlist")
    print("2. Add Song")
    print("3. Remove Song")
    print("4. Repeat Playlist")
    print("5. Search Song")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_playlist()
    elif choice == "2":
        add_song()
    elif choice == "3":
        remove_song()
    elif choice == "4":
        repeat_playlist()
    elif choice == "5":
        search_song()
    elif choice == "6":
        print("Exiting Playlist Creator. Enjoy your music!")
        break
    else:
        print("Invalid choice.")
