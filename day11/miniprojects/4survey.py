# 4. Survey Response Filter

# Goal: Clean up survey responses for analysis.
# Requirements:
# - Store each response ID in a set.
# - Add new responses with update().
# - Remove invalid responses with remove() and discard().
# - Track removed responses separately.
# - Use pop() to test random removal.
# Concepts Covered: update(), remove(), discard(), pop()

# Step 1: Initial set of response IDs
responses = {"ID001", "ID002", "ID003"}
print("Initial responses:", responses)

# Step 2: Add new responses with update()
responses.update(["ID004", "ID005"])
print("After update:", responses)

# Step 3: Remove invalid responses with remove() (tracked) and discard()
removed_invalid = []
try:
    responses.remove("ID002")  
    removed_invalid.append("ID002")
except KeyError:
    print("ID002 not present")

# Using discard on a non-existent ID 
responses.discard("ID999")
print("After remove/discard:", responses)
print("Removed invalid:", removed_invalid)

# Step 4: Use pop() to simulate random check/removal
random_id = responses.pop()
print("Randomly popped:", random_id)
print("Remaining responses:", responses)
print("Total responses now:", len(responses))
