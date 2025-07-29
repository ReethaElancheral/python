# 16. Chatbot (Rule-Based) 
# Objective: Answer FAQs using keyword matching. 
# Requirements: 
#  OOP: Chatbot class (responses dictionary). 
#  Dictionary: {"hi": "Hello!", ...}. 
#  File Handling: Load responses from JSON. 
#  Exception Handling: Handle unknown queries. 
#  String Operations: Case-insensitive matching. 
#  Loops: Continuous chat until "exit". 
#  Conditionals: Check for keywords. 
#  Generator: Yield possible responses. 
#  Decorator: @log_chat to save conversations.

from chatbot.core import Chatbot

def main():
    print("🤖 Welcome to the CLI Chatbot! Type 'exit' to quit.")
    bot = Chatbot()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("🤖 Bot: Goodbye!")
            break

        response = bot.get_response(user_input)
        print(f"🤖 Bot: {response}")

if __name__ == "__main__":
    main()
