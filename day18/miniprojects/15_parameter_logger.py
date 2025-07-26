# 15. Parameter Logger for CLI Tools 
# Objective: Log command-line arguments passed to a CLI function. 
# Requirements: 
#  Use *args and **kwargs in decorator 
#  Store logs in JSON format 
#  Maintain parameter history 

import time
import json
from functools import wraps

cli_param_logs = []

def cli_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_entry = {
            "function": func.__name__,
            "args": args,
            "kwargs": kwargs,
            "timestamp": time.time()
        }
        cli_param_logs.append(log_entry)
        with open("cli_logs.json", "w") as f:
            json.dump(cli_param_logs, f, indent=4)
        return func(*args, **kwargs)
    return wrapper

@cli_logger
def run_cli_tool(command, **options):
    print(f"Running: {command} with options {options}")

# Example:
run_cli_tool("backup", path="/home/user", recursive=True)
