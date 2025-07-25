# 12. Chatbot Typing Simulation 
# Objective: Simulate chatbot typing effect with delays using generators. 
# Requirements: 
#  Yield one character at a time from a message. 
#  Add delay using time.sleep() inside generator. 
#  Accept input with send() to interrupt or skip. 

import time

def chatbot_typing_simulator(message):
    i = 0
    while i < len(message):
        interrupt = yield message[i]
        if interrupt == "skip":
            break
        time.sleep(0.2)
        i += 1

# Example usage
chat = chatbot_typing_simulator("Hello, how can I assist you?")
print("Chatbot is typing:")
try:
    while True:
        print(next(chat), end='', flush=True)
except StopIteration:
    print("\nDone")
