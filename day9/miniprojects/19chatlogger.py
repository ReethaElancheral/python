# 19. Chat Conversation Logger

# Goal: Store chat messages for a user.
# Requirements:
# Each message: (timestamp, (sender, message))
# Use slicing to get recent messages.
# Tuple unpacking to format display.
# Prevent edit using immutability.

from datetime import datetime


chat_log = []


def add_message(sender, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat_log.append((timestamp, (sender, message)))

def display_recent_messages(n):
    print(f"\n🗨️ Last {n} Messages")
    print("----------------------")
    for timestamp, (sender, message) in chat_log[-n:]:
        print(f"[{timestamp}] {sender}: {message}")
    print("----------------------")


def count_messages_by_sender(sender):
    return sum(1 for _, (s, _) in chat_log if s == sender)


add_message("Alice", "Hello, how are you?")
add_message("Bob", "I'm good, thanks!")
add_message("Alice", "Great to hear!")


display_recent_messages(2)


alice_message_count = count_messages_by_sender("Alice")
print(f"\n✅ Alice has sent {alice_message_count} messages.")
