import json
from datetime import datetime

def log_chat(func):
    def wrapper(self, user_input):
        response = func(self, user_input)
        with open("chat_log.txt", "a") as f:
            f.write(f"{datetime.now()} | User: {user_input} | Bot: {response}\n")
        return response
    return wrapper

class Chatbot:
    def __init__(self, responses_file="responses.json"):
        self.responses = {}
        self.load_responses(responses_file)

    def load_responses(self, filename):
        try:
            with open(filename, "r") as f:
                self.responses = json.load(f)
        except Exception as e:
            print(f"⚠️ Failed to load responses: {e}")
            self.responses = {}

    @log_chat
    def get_response(self, user_input):
        user_input_lower = user_input.lower()
        for keyword, response in self.generate_responses():
            if keyword in user_input_lower:
                return response
        return "Sorry, I don't understand that."

    def generate_responses(self):
        for keyword, response in self.responses.items():
            yield keyword.lower(), response
