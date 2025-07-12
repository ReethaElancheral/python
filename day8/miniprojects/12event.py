# 12. Event Guest List Manager

# Description: Track guest names for an event.
# Add/remove guests.
# Print total guests using len().
# Check if a guest is invited using in.



guest_list = []

def show_guests():
    if not guest_list:
        print("No guests have been invited yet.")
    else:
        print("\n📋 Guest List:")
        for i, guest in enumerate(guest_list, 1):
            print(f"{i}. {guest}")

def add_guest():
    name = input("Enter guest name to add: ").strip()
    if name in guest_list:
        print(f"{name} is already on the guest list.")
    else:
        guest_list.append(name)
        print(f"{name} has been added to the guest list.")

def remove_guest():
    name = input("Enter guest name to remove: ").strip()
    if name in guest_list:
        guest_list.remove(name)
        print(f"{name} has been removed from the guest list.")
    else:
        print(f"{name} is not on the guest list.")

def check_guest():
    name = input("Enter guest name to check: ").strip()
    if name in guest_list:
        print(f"Yes, {name} is invited.")
    else:
        print(f"No, {name} is not invited.")


while True:
    print("\n--- Event Guest List Manager ---")
    print("1. Show Guests")
    print("2. Add Guest")
    print("3. Remove Guest")
    print("4. Check if Invited")
    print("5. Total Guests")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_guests()
    elif choice == "2":
        add_guest()
    elif choice == "3":
        remove_guest()
    elif choice == "4":
        check_guest()
    elif choice == "5":
        print(f"Total guests invited: {len(guest_list)}")
    elif choice == "6":
        print("Exiting Guest List Manager. Goodbye!")
        break
    else:
        print("Invalid option.")
