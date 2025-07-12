# 23. Mini File Organizer (Mock)

# Concepts: string list, functions.
# Input file names.
# Categorize by extension (.jpg, .txt).
# Show summary.


def categorize_files(file_list):
    categories = {}
    for file in file_list:
        if '.' in file:
            ext = file.split('.')[-1].lower()
            if ext not in categories:
                categories[ext] = []
            categories[ext].append(file)
        else:
            if 'no_extension' not in categories:
                categories['no_extension'] = []
            categories['no_extension'].append(file)
    return categories

def show_summary(categories):
    print("\n--- File Summary by Extension ---")
    for ext, files in categories.items():
        print(f".{ext} ({len(files)} file(s)): {', '.join(files)}")


file_input = input("Enter file names separated by commas: ")
file_list = [f.strip() for f in file_input.split(',') if f.strip()]

categorized = categorize_files(file_list)
show_summary(categorized)
