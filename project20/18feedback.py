# ✅ 18. Feedback Analyzer

# Objective: Classify feedback messages.
# Requirements:
# Input: list of messages (strings).
# Use for loop to classify:
# If message contains “good” → Positive
# Else → Neutral

messages_input = input("Enter feedback messages separated by commas: ").split(',')

print("\nFeedback Classification:")
for msg in messages_input:
    msg_clean = msg.strip().lower()
    if "good" in msg_clean:
        classification = "Positive"
    else:
        classification = "Neutral"
    print(f"'{msg.strip()}' → {classification}")
