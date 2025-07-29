# 25. Music Playlist Manager 
# Objective: Manage song playlists. 
# Requirements: 
#  OOP: Playlist class (songs, current_index). 
#  List: Store songs. 
#  File Handling: Save playlists to JSON. 
#  Functions: add_song(), shuffle(). 
#  Exception Handling: Invalid file paths. 
#  Generator: Yield next song. 
#  Decorator: @repeat for looped playlists.


from playlist_manager.core import Playlist

def main():
    print("🎶 Welcome to Music Playlist Manager")
    playlist = Playlist()

    while True:
        print("\nOptions:")
        print("1. Add song")
        print("2. Shuffle playlist")
        print("3. Save playlist")
        print("4. Load playlist")
        print("5. Play next song")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            song = input("Enter song name to add: ").strip()
            try:
                playlist.add_song(song)
                print(f"✅ Added '{song}' to playlist.")
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == "2":
            playlist.shuffle()
            print("🔀 Playlist shuffled.")

        elif choice == "3":
            path = input("Enter filename to save playlist: ").strip()
            try:
                playlist.save_to_file(path)
                print(f"💾 Playlist saved to '{path}'.")
            except Exception as e:
                print(f"❌ Could not save playlist: {e}")

        elif choice == "4":
            path = input("Enter filename to load playlist: ").strip()
            try:
                playlist.load_from_file(path)
                print(f"📂 Playlist loaded from '{path}'.")
            except Exception as e:
                print(f"❌ Could not load playlist: {e}")

        elif choice == "5":
            try:
                # Create a generator for the playlist songs
                gen = playlist.next_song()
                print(f"▶️ Now playing: {next(gen)}")
            except StopIteration as e:
                print(f"❌ {e}")

        elif choice == "6":
            print("Goodbye! 🎵")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
