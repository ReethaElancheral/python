import os

def create_backup(source_path):
    try:
        if not os.path.isfile(source_path):
            print("❌ File not found.")
            return

        # Extract name and extension
        base, ext = os.path.splitext(source_path)
        backup_path = f"{base}_backup{ext}"

        if os.path.exists(backup_path):
            print(f"⚠️ Backup file already exists: {backup_path}")
            return

        with open(source_path, "r") as original:
            content = original.read()

        with open(backup_path, "w") as backup:
            backup.write(content)

        print(f"✅ Backup created successfully: {backup_path}")

    except FileNotFoundError:
        print("❌ The file does not exist.")
    except PermissionError:
        print("❌ Permission denied to read/write the file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
