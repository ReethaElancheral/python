import os

def save_resume(content, filename, format="text"):
    ext = "md" if format == "markdown" else "txt"
    out_file = f"{filename}.{ext}"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Resume saved to {out_file}")
