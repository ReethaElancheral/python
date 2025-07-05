# ✅ 19. Character Position Identifier


# Objective: Print character and its index in a name.
# Requirements:
# Input: name.
# Use enumerate() to print like:
# python-replCopyEdit0 - M  
# 1 - a  
# 2 - h... 


name = input("Enter your name: ")

print("\nCharacter Positions:")
for index, char in enumerate(name):
    print(f"{index} - {char}")
