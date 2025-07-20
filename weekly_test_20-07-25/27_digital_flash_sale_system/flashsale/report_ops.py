def generate_report(sales):
    if not sales:
        print("\nNo sales recorded.")
        return

    print("\n=== Sales Report ===")
    buyers = set()
    for product_code, buyer, qty, time in sales:
        buyers.add(buyer)
        print(f"{time}: {buyer} bought {qty} of {product_code}")
    
    print(f"\nTotal Unique Buyers: {len(buyers)}")
