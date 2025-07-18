# journal/main.py

import argparse
from journal.entry import log_entry
from journal.viewer import search_entries
from journal.exporter import export_entries

def main():
    parser = argparse.ArgumentParser(description="Daily Journal CLI App")
    parser.add_argument("action", choices=["log", "search", "export"], help="Action to perform")
    parser.add_argument("-k", "--keyword", help="Keyword to search for in entries")
    parser.add_argument("-e", "--entry", help="Content of the journal entry to log")

    args = parser.parse_args()

    if args.action == "log":
        if args.entry:
            log_entry(args.entry)
        else:
            print("Please provide the entry content using -e or --entry.")
    elif args.action == "search":
        if args.keyword:
            search_entries(args.keyword)
        else:
            print("Please provide a keyword using -k or --keyword.")
    elif args.action == "export":
        export_entries()

if __name__ == "__main__":
    main()
