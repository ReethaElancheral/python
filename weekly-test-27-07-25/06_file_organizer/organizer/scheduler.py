import threading
import time
from .organize import organize_by_extension

def schedule_organization(folder_path, interval_seconds):
    def task():
        while True:
            print("Running scheduled organization...")
            organize_by_extension(folder_path)
            time.sleep(interval_seconds)

    t = threading.Thread(target=task, daemon=True)
    t.start()
    print(f"Scheduled organization every {interval_seconds} seconds.")
