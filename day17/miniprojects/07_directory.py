# 7. Directory File Scanner 
# Objective: Recursively walk through all files in a directory using a generator. 
# Requirements: 
#  Use os.walk and yield files one-by-one. 
#  Use generator expression to filter .txt files. 
#  Stop after N files using StopIteration.


import os

def directory_file_scanner(directory, max_files):
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            yield full_path
            count += 1
            if count >= max_files:
                return  # Triggers StopIteration

# Example usage:
directory = "."  # Current directory
scanner = directory_file_scanner(directory, 5)
txt_files = (f for f in scanner if f.endswith(".txt"))

print("Scanning .txt files (max 5):")
for file in txt_files:
    print(file)
