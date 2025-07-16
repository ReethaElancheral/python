# 8. Language Translator

# Description: English to Tamil dictionary.
# Requirements:
# - Structure: {english_word: tamil_word}
# - Allow adding, updating, and deleting translations
# - Search and return Tamil word using .get()
# - Reverse translation using swapped dictionary
# - Use in to check availability


translator = {
    "hello": "வணக்கம்",
    "thank you": "நன்றி",
    "yes": "ஆம்",
    "no": "இல்லை"
}

def add_translation(english, tamil):
    """Add a new translation or update an existing one."""
    translator[english] = tamil

def delete_translation(english):
    """Delete an existing translation."""
    translator.pop(english, None)

def translate_to_tamil(english):
    """Translate English to Tamil using .get() with a default."""
    return translator.get(english.lower(), "மொழிபெயர்ப்பு கிடைக்கவில்லை")

def reverse_translator():
    """Generate Tamil → English dictionary."""
    return {ta: en for en, ta in translator.items()}

def translate_to_english(tamil):
    rev = reverse_translator()
    return rev.get(tamil, "Translation not found")

add_translation("good morning", "காலை வணக்கம்")


delete_translation("yes")


print(translate_to_tamil("hello"))        
print(translate_to_tamil("Good Night"))  


print(translate_to_english("நன்றி"))     
print(translate_to_english("வணக்கம்"))   


print("thank you" in translator)  
