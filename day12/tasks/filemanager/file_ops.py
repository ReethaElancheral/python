import shutil, os
from pathlib import Path

def copy(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"Copied {src} → {dst}")
    except shutil.SameFileError:
        print("Source and destination are the same.")
    except Exception as e:
        print("Copy error:", e)

def move(src, dst):
    try:
        shutil.move(src, dst)
        print(f"Moved {src} → {dst}")
    except Exception as e:
        print("Move error:", e)

def delete(path):
    p = Path(path)
    if p.is_dir():
        shutil.rmtree(p)
        print(f"Deleted directory {path}")
    elif p.is_file():
        p.unlink()
        print(f"Deleted file {path}")
