import os

def scan_directory(directory):
    files_by_type = {}

    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        if os.path.isfile(path):
            _, ext = os.path.splitext(entry)
            ext = ext.lower().strip('.')
            files_by_type.setdefault(ext, []).append(entry)

    return files_by_type
