import sys
from resume import input, template, export

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <json_file> [text|markdown]")
        return

    filepath = sys.argv[1]
    format = sys.argv[2] if len(sys.argv) > 2 else "text"

    try:
        data = input.load_resume_data(filepath)
        result = template.generate_resume(data, format=format)
        export.save_resume(result, "output_resume", format=format)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
