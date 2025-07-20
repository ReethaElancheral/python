from chat.user_ops import add_user
from chat.chat_ops import send_message, view_chat, delete_chat

def main():
    users = set()
    chat_logs = {}

    while True:
        print("\n--- Simple Chat App ---")
        print("1. Add User")
        print("2. Send Message")
        print("3. View Chat")
        print("4. Delete Chat")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter new username: ")
            add_user(users, username)

        elif choice == '2':
            sender = input("Sender: ")
            receiver = input("Receiver: ")
            message = input("Message: ")
            send_message(users, chat_logs, sender, receiver, message)

        elif choice == '3':
            u1 = input("User 1: ")
            u2 = input("User 2: ")
            view_chat(chat_logs, u1, u2)

        elif choice == '4':
            u1 = input("User 1: ")
            u2 = input("User 2: ")
            delete_chat(chat_logs, u1, u2)

        elif choice == '5':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
