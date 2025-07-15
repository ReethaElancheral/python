# 5. Product Inventory System

# Goal: Store product details using tuples.
# Requirements:
# Each product: (product_id, name, price, in_stock)
# Use tuple operations to find total inventory value.
# Filter products using for loop and conditions.
# Sort products by price using sorted().
# Print reports with unpacked tuple values.

products = [
    (101, "Pen", 1.5, True),
    (102, "Notebook", 3.0, True),
    (103, "Eraser", 0.5, False),
    (104, "Pencil", 1.0, True)
]

def total_inventory_value(product_list):
   
    return sum(p[2] for p in product_list if p[3])

def filter_in_stock(product_list):

    return [p for p in product_list if p[3]]

def sort_by_price(product_list):
    
    return sorted(product_list, key=lambda x: x[2]) 

def print_report(product_list):
  
    print("\n📦 Product Inventory Report")
    print("----------------------------")
    for prod_id, name, price, in_stock in product_list:
        status = "Available" if in_stock else "Out of stock"
        print(f"ID: {prod_id} | {name} | Price: ₹{price:.2f} | {status}")
    print("----------------------------\n")


print_report(products)

total_value = total_inventory_value(products)
print(f"Total inventory value (for in-stock items): ₹{total_value:.2f}")

in_stock = filter_in_stock(products)
print_report(in_stock)

sorted_products = sort_by_price(products)
print("Products sorted by price:")
print_report(sorted_products)
