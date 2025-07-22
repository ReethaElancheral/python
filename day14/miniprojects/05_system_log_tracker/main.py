from systemlog.logger import track_function_call
from systemlog.display import show_banner
import time

def my_function():
    print("🟢 Function executed.")
    track_function_call("my_function")

def main():
    show_banner()
    for _ in range(12):
        my_function()
        time.sleep(1)  # simulate delay

if __name__ == "__main__":
    main()
