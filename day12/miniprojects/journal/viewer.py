# journal/viewer.py

import os
import re
import fnmatch
from datetime import datetime

def search_entries(keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    for filename in os.listdir("journal/data"):
        if fnmatch.fnmatch(filename, "*.txt"):
            with open(os.path.join("journal/data", filename), "r") as file:
                content = file.read()
                if pattern.search(content):
                    print(f"Found in {filename}:")
                    print(content)
