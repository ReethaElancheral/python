# 🧩 17. Chat Formatter

# Topics Covered: string manipulation, map(), lambda, return
# Requirements:
# Function accepts multiple messages
# Return messages capitalized, with timestamps (hardcoded or generated)
# Use map() with lambda for formatting

from datetime import datetime

def chat_formatter(*messages):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    formatted = map(lambda msg: f"[{timestamp}] {msg.capitalize()}", messages)
    

    return list(formatted)

msgs = ["hello there", "how are you?", "goodbye!"]
formatted_msgs = chat_formatter(*msgs)
for fm in formatted_msgs:
    print(fm)
