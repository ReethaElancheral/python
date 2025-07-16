# 13. Duplicate SKU Checker for 

# Goal: Identify duplicate product SKUs in stock.
# Requirements:
# - Convert SKU list to a set.
# - Compare lengths of original list and set to detect duplicates.
# - Store duplicates separately.
# Concepts Covered: Set creation, len(), membership.

# Sample list of SKUs (with duplicates)
sku_list = [
    "A123", "B456", "C789", "A123", "D012", "B456", "E345", "F678", "G901", "C789"
]

# Convert list to set to remove duplicates
sku_set = set(sku_list)

# Identify duplicates by comparing lengths
duplicates = [sku for sku in sku_set if sku_list.count(sku) > 1]


print("Original SKU List:", sku_list)
print("Unique SKUs:", sku_set)
print("Duplicate SKUs:", duplicates)
