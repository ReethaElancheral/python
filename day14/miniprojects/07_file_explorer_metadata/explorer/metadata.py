import os
from datetime import datetime

REPORT_DIR = "reports"

def format_datetime(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def scan_folder_and_export(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder not found.")
        return

    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    report_name = datetime.now().strftime("report_%Y%m%d_%H%M%S.txt")
    report_path = os.path.join(REPORT_DIR, report_name)

    try:
        with open(report_path, "w") as report:
            report.write(f"📁 Folder Scanned: {folder_path}\n")
            report.write(f"{'-'*60}\n")
            report.write(f"{'Filename':30} {'Size (bytes)':15} {'Created':20} {'Modified':20}\n")
            report.write(f"{'-'*60}\n")

            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    size = os.path.getsize(file_path)
                    created = format_datetime(os.path.getctime(file_path))
                    modified = format_datetime(os.path.getmtime(file_path))
                    report.write(f"{filename:30} {size:<15} {created} {modified}\n")

        print(f"✅ Metadata exported to {report_path}")
    except Exception as e:
        print(f"❌ Error generating report: {e}")
