import os

BASE_DIR = "notes_data"

def add_note():
    category = input("Enter category (e.g., Work, Personal): ").strip()
    note_title = input("Enter note title: ").strip()
    note_content = input("Enter note content:\n").strip()

    category_path = os.path.join(BASE_DIR, category)
    os.makedirs(category_path, exist_ok=True)

    filename = f"{note_title}.txt"
    filepath = os.path.join(category_path, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(note_content)
    print(f"✅ Note saved under '{category}/{filename}'")

def view_notes():
    category = input("Enter category to view notes: ").strip()
    category_path = os.path.join(BASE_DIR, category)
    if not os.path.exists(category_path):
        print("❌ No such category found.")
        return

    files = os.listdir(category_path)
    if not files:
        print("No notes found in this category.")
        return

    print(f"Notes in category '{category}':")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    choice = input("Enter note number to read or '0' to exit: ").strip()
    if choice == "0":
        return

    try:
        choice = int(choice)
        if 1 <= choice <= len(files):
            filepath = os.path.join(category_path, files[choice - 1])
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"\n--- {files[choice - 1]} ---\n{content}\n")
        else:
            print("❌ Invalid note number.")
    except ValueError:
        print("❌ Invalid input.")

def search_notes():
    keyword = input("Enter keyword to search in all notes: ").strip().lower()
    if not os.path.exists(BASE_DIR):
        print("❌ No notes found.")
        return

    found = False
    for category in os.listdir(BASE_DIR):
        category_path = os.path.join(BASE_DIR, category)
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                filepath = os.path.join(category_path, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                    if keyword in content or keyword in file.lower():
                        print(f"Found in '{category}/{file}':")
                        snippet = content[:100].replace("\n", " ")  # first 100 chars
                        print(f"  ...{snippet}...\n")
                        found = True
    if not found:
        print("No notes matched your search.")
