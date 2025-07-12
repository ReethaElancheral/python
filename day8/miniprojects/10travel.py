# 10. Travel Bucket List

# Description: Maintain a list of places a user wants to visit.
# Add, remove, update places.
# Display all places.
# Use in to check if a place is already on the list.



bucket_list = []

def show_places():
    if not bucket_list:
        print("Your travel bucket list is empty.")
    else:
        print("\n🌍 Places you want to visit:")
        for i, place in enumerate(bucket_list, 1):
            print(f"{i}. {place}")

def add_place():
    place = input("Enter a place to add: ").strip()
    if place in bucket_list:
        print(f"{place} is already in your bucket list.")
    else:
        bucket_list.append(place)
        print(f"{place} added to your bucket list.")

def remove_place():
    place = input("Enter a place to remove: ").strip()
    if place in bucket_list:
        bucket_list.remove(place)
        print(f"{place} removed from your bucket list.")
    else:
        print(f"{place} is not in your bucket list.")

def update_place():
    show_places()
    if not bucket_list:
        return
    index = input("Enter the number of the place to update: ")
    if index.isdigit():
        index = int(index) - 1
        if 0 <= index < len(bucket_list):
            new_place = input("Enter the new place name: ").strip()
            if new_place in bucket_list:
                print(f"{new_place} is already in the list.")
            else:
                old_place = bucket_list[index]
                bucket_list[index] = new_place
                print(f"{old_place} updated to {new_place}.")
        else:
            print("Invalid number.")
    else:
        print("Please enter a valid number.")


while True:
    print("\n--- Travel Bucket List Menu ---")
    print("1. Show all places")
    print("2. Add a place")
    print("3. Remove a place")
    print("4. Update a place")
    print("5. Exit")

    choice = input("Choose an option (1–5): ")

    if choice == "1":
        show_places()
    elif choice == "2":
        add_place()
    elif choice == "3":
        remove_place()
    elif choice == "4":
        update_place()
    elif choice == "5":
        print("Safe travels! ✈️")
        break
    else:
        print("Invalid option.")
