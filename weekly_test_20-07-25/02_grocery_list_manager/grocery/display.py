

def show_items(data, bought):
    print("\nGrocery List by Category:")
    for cat, items in data.items():
        print(f"\nCategory: {cat}")
        for item in items:
            mark = "[✓]" if item[0] in bought else "[ ]"
            print(f"  {mark} {item[0]}")
