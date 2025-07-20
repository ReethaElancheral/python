from datetime import datetime

def list_products(products):
    print("\nAvailable Products:")
    for code, info in products.items():
        print(f"{code}: {info['name']} - ₹{info['price']}")

def add_sale(products, sales, product_code, buyer, qty):
    if product_code not in products:
        print("Invalid product code.")
        return

    price = products[product_code]['price']
    
    # Apply discount conditionally
    if qty >= 3:
        print("Applied 10% discount.")
        price *= 0.9

    total = price * qty
    time_of_sale = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sale = (product_code, buyer, qty, time_of_sale)
    sales.append(sale)
    
    print(f"Sale recorded: {products[product_code]['name']} x{qty} for ₹{total:.2f}")
