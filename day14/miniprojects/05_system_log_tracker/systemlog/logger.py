import os
from datetime import datetime

LOG_DIR = "logs"

def get_log_file():
    today = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    return os.path.join(LOG_DIR, f"{today}.log")

def count_lines(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path, "r") as f:
        return sum(1 for _ in f)

def rotate_log(file_path):
    if os.path.exists(file_path) and count_lines(file_path) >= 10:
        timestamp = datetime.now().strftime("%H%M%S")
        base, ext = os.path.splitext(file_path)
        new_path = f"{base}_{timestamp}{ext}"
        os.rename(file_path, new_path)
        print(f"🔁 Log rotated to {new_path}")

def track_function_call(func_name):
    log_path = get_log_file()
    rotate_log(log_path)

    with open(log_path, "a") as log_file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{now}] Function executed: {func_name}\n")
        print(f"📄 Log written to {log_path}")
