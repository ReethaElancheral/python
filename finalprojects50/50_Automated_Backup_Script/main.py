import os
import zipfile
from datetime import datetime
import time
import threading

def zip_directory(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        total_files = 0
        for root, _, files in os.walk(source_dir):
            total_files += len(files)
        count = 0
        for root, _, files in os.walk(source_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, source_dir)
                zipf.write(filepath, arcname)
                count += 1
                print(f"Zipped {count}/{total_files} files...", end='\r')
    print(f"\nBackup completed: {output_filename}")

def schedule_backup(source_dir, interval_seconds):
    def backup_job():
        while True:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"backup_{timestamp}.zip"
            print(f"Starting backup at {timestamp}...")
            zip_directory(source_dir, output_filename)
            print(f"Waiting {interval_seconds} seconds for next backup...")
            time.sleep(interval_seconds)

    t = threading.Thread(target=backup_job, daemon=True)
    t.start()

def main():
    print("Automated Backup Script")
    source_dir = input("Enter directory to backup: ").strip()
    if not os.path.isdir(source_dir):
        print("Invalid directory path.")
        return
    interval = input("Enter backup interval in seconds: ").strip()
    try:
        interval_seconds = int(interval)
        if interval_seconds <= 0:
            raise ValueError
    except ValueError:
        print("Invalid interval. Must be a positive integer.")
        return

    print("Starting automated backups. Press Ctrl+C to stop.")
    schedule_backup(source_dir, interval_seconds)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBackup process stopped by user.")

if __name__ == "__main__":
    main()
