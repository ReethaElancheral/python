import os
import difflib

def load_document(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def compare_texts(text1, text2):
    seq = difflib.SequenceMatcher(None, text1, text2)
    return seq.ratio()  # Returns a float between 0 and 1

def main():
    print("Plagiarism Checker")

    doc1_path = input("Enter path for first document: ").strip()
    doc2_path = input("Enter path for second document: ").strip()

    if not os.path.isfile(doc1_path) or not os.path.isfile(doc2_path):
        print("One or both files do not exist.")
        return

    text1 = load_document(doc1_path)
    text2 = load_document(doc2_path)

    if text1 is None or text2 is None:
        print("Could not read one or both documents.")
        return

    similarity = compare_texts(text1, text2)
    percentage = similarity * 100
    print(f"\nSimilarity between documents: {percentage:.2f}%")

    if percentage > 0.75:
        print("Warning: Documents are highly similar. Potential plagiarism detected.")
    else:
        print("Documents are sufficiently different.")

if __name__ == "__main__":
    main()
