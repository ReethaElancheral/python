# 🧩 10. Personal Diary Entry Tool

# Topics Covered: inner functions, file handling (optional), return
# Requirements:
# Main function accepts entry
# Inner function saves or prints entry
# Return length of entry and word count

def diary_entry_tool(entry, save_to_file=False, filename="diary.txt"):
    def save_or_print(text):
        if save_to_file:
            with open(filename, "a") as file:
                file.write(text + "\n")
        else:
            print("Diary Entry:\n", text)

    save_or_print(entry)

 
    length = len(entry)
    word_count = len(entry.split())

    return length, word_count

entry_text = "Today I learned about inner functions in Python."
length, words = diary_entry_tool(entry_text, save_to_file=False)

print(f"Entry length: {length} characters")
print(f"Word count: {words}")
