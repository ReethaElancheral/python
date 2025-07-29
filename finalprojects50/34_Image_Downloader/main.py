import os
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse
from functools import wraps

def download_progress(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting download...")
        result = func(*args, **kwargs)
        print("Download complete.")
        return result
    return wrapper

class ImageDownloader:
    def __init__(self, save_dir="downloaded_images"):
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)
        self.queue = []

    def add_url(self, url):
        self.queue.append(url)

    @download_progress
    def download_all(self):
        for url in self.queue:
            try:
                self.download_image(url)
            except Exception as e:
                print(f"Failed to download {url}: {e}")

    def download_image(self, url):
        print(f"Downloading: {url}")
        response = requests.get(url)
        response.raise_for_status()

        # Validate image by opening with PIL
        image = Image.open(BytesIO(response.content))
        ext = image.format.lower()
        if ext not in ['jpeg', 'jpg', 'png', 'gif', 'bmp']:
            ext = 'jpg'  # default extension

        # Extract filename from URL or generate unique name
        path = urlparse(url).path
        filename = os.path.basename(path)
        if not filename or '.' not in filename:
            filename = f"image_{int(time.time())}.{ext}"

        save_path = os.path.join(self.save_dir, filename)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Saved to {save_path}")

    def __iter__(self):
        return self.generator()

    def generator(self):
        for url in self.queue:
            yield url

def main():
    downloader = ImageDownloader()

    print("Image Downloader CLI")
    print("Enter image URLs one per line. Type 'done' to start downloading.")

    while True:
        url = input("Image URL: ").strip()
        if url.lower() == 'done':
            break
        if url:
            downloader.add_url(url)

    if not downloader.queue:
        print("No URLs provided. Exiting.")
        return

    print("\nURLs to download:")
    for u in downloader:
        print(u)

    downloader.download_all()

if __name__ == "__main__":
    import time
    main()

