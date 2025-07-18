def generate_report(moved_files):
    print("\nOrganizing Report:")
    print("=" * 40)
    for category, files in moved_files.items():
        print(f"{category.upper()} ({len(files)} files):")
        for f in files:
            print(f"  - {f}")
        print("-" * 40)
