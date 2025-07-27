import os
import shutil

def organize_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError("Provided path is not a directory.")

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1][1:].lower() or "no_extension"
            target_folder = os.path.join(folder_path, ext)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(target_folder, filename))
    print("Files organized by extension.")
