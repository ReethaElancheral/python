# 15. File Type Counter

# Description: Count file types from a list of filenames.
# Requirements:
# - Input: List of filenames
# - Output: Dictionary of file extensions and their counts
# - Use split() and .get() to update dictionary


files = [
    "document1.txt", "image1.jpg", "document2.txt", "image2.png",
    "image3.jpg", "audio.mp3", "audio.wav", "image4.png"
]

def count_file_types(filenames):
    """Count occurrences of each file extension."""
    return {
        ext: filenames.count(ext)
        for ext in set(filenames)
    }

file_extensions = [file.split('.')[-1] for file in files if '.' in file]


extension_counts = count_file_types(file_extensions)

print("File Type Counts:", extension_counts)
