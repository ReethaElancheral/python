# 11. News Source Deduplication

# Goal: Identify and remove duplicate headlines.
# Requirements:
# - Convert fetched headlines from multiple APIs to sets.
# - Compare duplicates using intersection().
# - Store unique headlines using union().
# Concepts Covered: intersection(), union(), membership.

# Simulate fetched headlines from three APIs
api1 = [
    "Global markets rally as tech stocks surge",
    "Scientists discover new exoplanet",
    "Elections draw record turnout"
]

api2 = [
    "Scientists discover new exoplanet",
    "New smartphone model released",
    "Global markets rally as tech stocks surge"
]

api3 = [
    "Weather alerts issued in coastal areas",
    "Elections draw record turnout",
    "Advances in AI continue"
]

# 1. Convert lists to sets
set1 = set(api1)
set2 = set(api2)
set3 = set(api3)

# 2. Identify duplicates between sources using intersection()
dupes_1_2 = set1.intersection(set2)
dupes_1_3 = set1.intersection(set3)
dupes_2_3 = set2.intersection(set3)

# Identify headlines that are in all three
common_all = set1.intersection(set2, set3)

# 3. Create a union of all unique headlines
all_unique = set1.union(set2, set3)


print("Duplicates between API1 & API2:", dupes_1_2)
print("Duplicates between API1 & API3:", dupes_1_3)
print("Duplicates between API2 & API3:", dupes_2_3)
print("Headlines present across all three APIs:", common_all)
print("All unique headlines:", all_unique)
