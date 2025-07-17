# users/auth.py
_users = {}

def register_user(username):
    _users[username] = []
    print(f"Registered user: {username}")

def get_user_posts(username):
    return _users.get(username, [])
