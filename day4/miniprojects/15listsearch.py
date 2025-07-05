# ✅ 15. List Search with Break

# Objective: Search for a product in a product list using a loop.
# Requirements:
# Input: product to search.
# If found, print “Product Found” and break.
# If not found after loop, use else to print “Not Found”.


products = ["milk", "eggs", "bread", "rice", "oil", "sugar"]

search_item = input("Enter product name to search: ").lower()


for product in products:
    if product == search_item:
        print("✅ Product Found")
        break
else:
    
    print("❌ Product Not Found")
