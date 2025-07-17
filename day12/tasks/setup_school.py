

from pathlib import Path


paths = [
    "school",
    "school/students",
    "school/teachers",
]


for folder in paths:
    dir_path = Path(folder)
    dir_path.mkdir(parents=True, exist_ok=True)  

    init_file = dir_path / "__init__.py"
    init_file.touch(exist_ok=True)  
