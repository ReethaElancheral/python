def _get_chat_key(user1, user2):
    return tuple(sorted((user1, user2)))

def send_message(users, chat_logs, sender, receiver, message):
    if sender not in users or receiver not in users:
        print("Both users must exist.")
        return
    key = _get_chat_key(sender, receiver)
    if key not in chat_logs:
        chat_logs[key] = []
    chat_logs[key].append(f"{sender}: {message}")
    print("Message sent.")

def view_chat(chat_logs, user1, user2):
    key = _get_chat_key(user1, user2)
    if key in chat_logs:
        print(f"Chat between {user1} and {user2}:")
        for msg in chat_logs[key]:
            print(msg)
    else:
        print("No chat history found.")

def delete_chat(chat_logs, user1, user2):
    key = _get_chat_key(user1, user2)
    if key in chat_logs:
        del chat_logs[key]
        print("Chat deleted.")
    else:
        print("No chat to delete.")
