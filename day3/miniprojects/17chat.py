# 17. Basic Chat Filter App

# Objective: Block messages containing banned words.
# Requirements:
# Predefined list of banned words.
# Use in operator.
# Use if to check if input contains a banned word.
# Print warning message.



banned_words = ["spam", "advertisement", "scam", "fake"]

message = input("Enter your message: ").lower()

found_banned_word = False

for banned_word in banned_words:
    if banned_word in message:
        found_banned_word = True
        break 

if found_banned_word:
    print("⚠️ Warning: Your message contains banned words and cannot be sent.")
else:
    print("✅ Message sent successfully!")

