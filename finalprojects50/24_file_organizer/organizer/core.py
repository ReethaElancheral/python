import os
import shutil
from functools import wraps

# Extension to folder mapping
EXTENSION_MAP = {
    "jpg": "Images",
    "png": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "txt": "Documents",
    "pdf": "Documents",
    "docx": "Documents",
    "xlsx": "Documents",
    "mp3": "Music",
    "wav": "Music",
    "mp4": "Videos",
    "mkv": "Videos",
    "zip": "Archives",
    "rar": "Archives",
}

def dry_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("🔍 DRY RUN: Showing what will be moved...\n")
        for file in func(*args, **kwargs):
            print(f"Would move: {file}")
    return wrapper

def get_extension(filename):
    return filename.split(".")[-1].lower()

def move_file(file_path, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    shutil.move(file_path, os.path.join(dest_dir, os.path.basename(file_path)))

def file_generator(directory):
    for item in os.listdir(directory):
        file_path = os.path.join(directory, item)
        if os.path.isfile(file_path):
            yield file_path

@dry_run
def organize(directory):
    for file_path in file_generator(directory):
        try:
            ext = get_extension(file_path)
            folder = EXTENSION_MAP.get(ext, "Others")
            dest_dir = os.path.join(directory, folder)
            yield f"{file_path} ➜ {dest_dir}"
        except PermissionError as e:
            print(f"Permission error: {e}")
