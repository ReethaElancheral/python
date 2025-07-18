import sys
from expenses_splitter import members, split, report

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py data.csv")
        return

    filepath = sys.argv[1]

    try:
        people = members.load_members(filepath)
        updated_people, total, share = split.calculate_split(people)
        report.print_report(updated_people, total, share)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
