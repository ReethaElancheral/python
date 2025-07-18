import os
import glob

FILE_TYPES = {
    'images': ['*.jpg', '*.jpeg', '*.png', '*.gif'],
    'documents': ['*.pdf', '*.docx', '*.txt'],
    'videos': ['*.mp4', '*.mov', '*.avi'],
    'music': ['*.mp3', '*.wav'],
    'archives': ['*.zip', '*.tar', '*.gz'],
    'others': ['*']
}

def scan_directory(path):
    categorized_files = {key: [] for key in FILE_TYPES}

    for category, patterns in FILE_TYPES.items():
        for pattern in patterns:
            files = glob.glob(os.path.join(path, pattern))
            if category != 'others':
                categorized_files[category].extend(files)

    # For 'others', include only files that don't belong to any other category
    all_categorized = set(f for files in categorized_files.values() for f in files)
    for file in glob.glob(os.path.join(path, '*')):
        if os.path.isfile(file) and file not in all_categorized:
            categorized_files['others'].append(file)

    return categorized_files
