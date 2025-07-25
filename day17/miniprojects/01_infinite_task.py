# 1. Infinite Task Scheduler 

# Objective: Build a generator that endlessly cycles through a list of background 
# tasks. 
# Requirements: 
#  Use an infinite generator to yield tasks repeatedly. 
#  Support manual iteration with next(). 
#  Stop with break after 10 iterations. 
#  Log execution time lazily (only when requested). 

import itertools
import time

def task_scheduler():
    tasks = ["Backup DB", "Cleanup Temp", "Send Emails", "Monitor Logs"]
    for task in itertools.cycle(tasks):
        yield task

# Simulate scheduler
scheduler = task_scheduler()

print("Infinite Task Scheduler (10 iterations):")
for i in range(10):
    task = next(scheduler)
    print(f"Task {i + 1}: {task}")
