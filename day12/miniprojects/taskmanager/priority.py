# taskmanager/priority.py

LEVELS = {"low": 1, "medium": 2, "high": 3}

def validate(level):
    lvl = level.lower()
    if lvl not in LEVELS:
        raise ValueError(f"Invalid priority: {level}")
    return lvl
