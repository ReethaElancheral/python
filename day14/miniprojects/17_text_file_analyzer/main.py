from analyzer.analyzer_core import analyze_file
from analyzer.display import show_banner

def main():
    show_banner()
    filepath = input("Enter file path to analyze: ").strip()
    analyze_file(filepath)

if __name__ == "__main__":
    main()
