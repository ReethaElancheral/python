# 14. Social Media Post Scheduler

# Description: Schedule and manage posts.
# Store post titles.
# Insert priority post using insert().
# Remove posted items with pop().



posts = []

def show_posts():
    if not posts:
        print("No posts scheduled.")
    else:
        print("\n🗓 Scheduled Posts:")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post}")

def add_post():
    title = input("Enter post title to add: ").strip()
    if title:
        posts.append(title)
        print(f"'{title}' added to schedule.")
    else:
        print("Post title cannot be empty.")

def insert_priority_post():
    title = input("Enter priority post title: ").strip()
    if title:
        posts.insert(0, title)
        print(f"'{title}' inserted at the top of schedule.")
    else:
        print("Post title cannot be empty.")

def remove_post():
    if not posts:
        print("No posts to remove.")
    else:
        removed = posts.pop(0)  
        print(f"'{removed}' removed from schedule.")


while True:
    print("\n--- Social Media Post Scheduler ---")
    print("1. Show Scheduled Posts")
    print("2. Add Post")
    print("3. Insert Priority Post")
    print("4. Remove Posted Post")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_posts()
    elif choice == "2":
        add_post()
    elif choice == "3":
        insert_priority_post()
    elif choice == "4":
        remove_post()
    elif choice == "5":
        print("Exiting Scheduler. Goodbye!")
        break
    else:
        print("Invalid choice.")
