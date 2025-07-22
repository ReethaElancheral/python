from chatlogger.logger import ChatLogger
from chatlogger.display import show_banner
import threading
import time

def main():
    show_banner()
    logger = ChatLogger()

    def auto_save_loop():
        while True:
            time.sleep(120)  # auto-save every 2 minutes
            logger.auto_save()

    threading.Thread(target=auto_save_loop, daemon=True).start()

    print("Type messages below. Type '/exit' to quit, '/delete' to clear log (admin only).")
    while True:
        msg = input("You: ").strip()
        if msg == "/exit":
            logger.save()
            print("Exiting chat logger.")
            break
        elif msg == "/delete":
            password = input("Enter admin password to delete logs: ").strip()
            if logger.delete_logs(password):
                print("✅ Logs deleted.")
            else:
                print("❌ Wrong password.")
        else:
            logger.log_message(msg)

if __name__ == "__main__":
    main()
