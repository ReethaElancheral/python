# ✅ 10. User Info Collector

# Objective: Collect 5 names and ages.
# Requirements:
# Use while loop to input names and ages.
# Skip if name is blank using continue.
# Store data in a dictionary.
# Use pass in future placeholder for email validation.

user_data = {}
count = 0

while count < 5:
    name = input("Enter name: ").strip()
    if name == "":
        print("Name cannot be blank. Skipping entry.")
        continue

    age = input("Enter age: ").strip()
    
    pass

    user_data[name] = age
    count += 1

print("\nCollected User Data:")
for name, age in user_data.items():
    print(f"{name}: {age} years")
