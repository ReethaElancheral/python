import os
import hashlib

def file_hash(filepath, chunk_size=1024*1024):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_and_remove_duplicates(folder_path):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                file_h = file_hash(filepath)
                if file_h in hashes:
                    duplicates.append(filepath)
                else:
                    hashes[file_h] = filepath
            except Exception as e:
                print(f"Error reading file {filepath}: {e}")

    for dup in duplicates:
        os.remove(dup)
        print(f"Removed duplicate: {dup}")

    print(f"Total duplicates removed: {len(duplicates)}")
