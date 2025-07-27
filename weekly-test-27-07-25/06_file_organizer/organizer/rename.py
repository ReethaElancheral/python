import os
import re

def bulk_rename(folder_path, pattern, replacement):
    if not os.path.isdir(folder_path):
        raise ValueError("Provided path is not a directory.")

    regex = re.compile(pattern)

    for filename in os.listdir(folder_path):
        new_name = regex.sub(replacement, filename)
        if new_name != filename:
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_name)
            os.rename(src, dst)
            print(f"Renamed: {filename} -> {new_name}")

    print("Bulk rename completed.")
