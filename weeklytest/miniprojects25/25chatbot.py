# 25. Simple Chatbot (Menu-Based)

# Concepts: string comparison, functions, loop.
# Handle inputs like "Hi", "What is your name?", etc.
# Respond using if-else or dictionary map.
# Exit on "bye".



def chatbot():
    print("\n--- Welcome to Simple Chatbot ---")
    print("Type your message or 'bye' to exit.")

    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "what is your name?": "I'm Chatbot 1.0",
        "how are you?": "I'm just a program, but I'm functioning well!",
        "bye": "Goodbye! Have a nice day!"
    }

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

     
        response = responses.get(user_input, "I'm not sure how to respond to that.")
        print(f"Chatbot: {response}")


chatbot()
