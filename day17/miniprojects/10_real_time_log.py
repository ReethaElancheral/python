# 10. Real-Time Log Stream Monitor 

# Objective: Monitor logs as they're appended to a file. 
# Requirements: 
#  Use generator to read last line from file every second. 
#  Yield lines containing keywords like ERROR or WARNING. 
#  Can be stopped externally via KeyboardInterrupt.


import time
import os

def log_stream_monitor(filepath, keyword=("ERROR", "WARNING")):
    with open(filepath, "r") as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue
            if any(k in line for k in keyword):
                yield line.strip()

# Example usage:
# Create sample log file
with open("log.txt", "a") as f:
    f.write("INFO: All systems normal.\n")

print("Monitoring log for ERROR/WARNING (Ctrl+C to stop):")
try:
    for log_line in log_stream_monitor("log.txt"):
        print("Alert:", log_line)
except KeyboardInterrupt:
    print("Stopped log monitoring.")
