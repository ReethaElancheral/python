def add_user(users, username):
    if username in users:
        print(f"User '{username}' already exists.")
    else:
        users.add(username)
        print(f"User '{username}' added successfully.")
