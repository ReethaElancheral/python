import os
from datetime import datetime

LOG_FILE = "chat_session.log"
ADMIN_PASSWORD = "admin123"  # simple password for demo

class ChatLogger:
    def __init__(self):
        self.messages = []

    def log_message(self, msg):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] You: {msg}"
        self.messages.append(entry)
        print(f"Logged: {entry}")

    def save(self):
        if not self.messages:
            print("No messages to save.")
            return
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            for msg in self.messages:
                f.write(msg + "\n")
        print(f"✅ Saved {len(self.messages)} messages to {LOG_FILE}")
        self.messages.clear()

    def auto_save(self):
        print("⏳ Auto-saving chat log...")
        self.save()

    def delete_logs(self, password):
        if password != ADMIN_PASSWORD:
            return False
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
            self.messages.clear()
            return True
        return False
