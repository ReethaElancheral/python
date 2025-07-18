# library/cli.py

import argparse
from .search import search_ebooks
from .reader import read_pdf, read_all_ebooks

def main():
    parser = argparse.ArgumentParser(description="eBook Library Organizer")
    parser.add_argument('--search', type=str, help="Search for eBooks by title")
    parser.add_argument('--list', action='store_true', help="List all eBooks")
    parser.add_argument('--read', type=str, help="Read an eBook by path")
    parser.add_argument('--read-all', action='store_true', help="Read all eBooks")
    
    args = parser.parse_args()

    if args.list:
        from .catalog import list_ebooks
        ebooks = list_ebooks()
        if not ebooks:
            print("No eBooks found.")
        else:
            print("eBooks found:")
            for eb in ebooks:
                print(f"  • {eb}")
    elif args.search:
        results = search_ebooks(args.search)
        if results:
            print("Matched eBooks:")
            for m in results:
                title = m.get('title') or m.get('path')
                print(f"  • {title}")
        else:
            print("No matching eBooks found.")
    elif args.read:
        read_pdf(args.read)
    elif args.read_all:
        read_all_ebooks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
