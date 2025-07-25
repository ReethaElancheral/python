# 2. Lazy Product Inventory Viewer 
# Objective: Display product details lazily from a large inventory database (mocked 
# as a list of dicts). 
# Requirements: 
#  Yield one product at a time using yield. 
#  Implement pagination (e.g., 5 products per scroll). 
#  Use StopIteration to end properly. 
#  Use generator expression to filter "out of stock" products.

def lazy_inventory_viewer(products, page_size=5):
    count = 0
    for product in products:
        if product["stock"] > 0:
            yield product
            count += 1
            if count % page_size == 0:
                input("Press Enter to see next page...")

# Simulated inventory (mock)
inventory = [
    {"id": 1, "name": "Laptop", "stock": 10},
    {"id": 2, "name": "Phone", "stock": 0},
    {"id": 3, "name": "Mouse", "stock": 3},
    {"id": 4, "name": "Keyboard", "stock": 0},
    {"id": 5, "name": "Monitor", "stock": 5},
    {"id": 6, "name": "Charger", "stock": 1},
    {"id": 7, "name": "Tablet", "stock": 4},
]

# Filter out-of-stock
available_inventory = (p for p in inventory if p["stock"] > 0)

# Use generator viewer
print("Lazy Inventory Viewer:")
for product in lazy_inventory_viewer(available_inventory):
    print(product)
