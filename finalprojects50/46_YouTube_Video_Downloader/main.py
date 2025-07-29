from pytube import YouTube
import os

def download_video(url, path="."):
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        print("Downloading...")
        stream.download(output_path=path)
        print(f"Downloaded to {os.path.abspath(path)}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("YouTube Video Downloader")
    while True:
        url = input("\nEnter YouTube video URL (or 'exit' to quit): ").strip()
        if url.lower() == "exit":
            break
        download_video(url)

if __name__ == "__main__":
    main()
