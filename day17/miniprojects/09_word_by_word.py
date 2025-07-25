# 9. Word-by-Word File Speaker 
# Objective: Read a paragraph file and yield one word at a time for audio playback 
# simulation. 
# Requirements: 
#  Use file iterator. 
#  Strip punctuation and split words. 
#  Yield words lazily to avoid memory issues with large files. 

import string

def word_by_word_speaker(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            line = line.translate(str.maketrans('', '', string.punctuation))
            for word in line.split():
                yield word

# Example usage:
# Create a sample file
with open("paragraph.txt", "w") as f:
    f.write("Hello world! This is a test file.\nIt has two lines.")

print("Speaking file word by word:")
for word in word_by_word_speaker("paragraph.txt"):
    print(word)
