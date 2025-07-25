# 16. Product Price Filter 
# Goal: Yield only products above ₹1000 from a dictionary. 
# Requirements: 
#  Use iter() over dictionary items 
#  Filter based on value 
#  Stop after all are processed 

def price_filter(products):
    for name, price in products.items():
        if price > 1000:
            yield (name, price)

# Usage & Output
products = {
    "Laptop": 55000,
    "Mouse": 450,
    "Keyboard": 900,
    "Monitor": 7200,
    "Charger": 1200
}

print("Products priced above ₹1000:")
for item, price in price_filter(products):
    print(f"{item}: ₹{price}")
