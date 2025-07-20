users_db = {
    "user1": {"password": "pass1", "balance": 1000.0, "transactions": []},
    "user2": {"password": "pass2", "balance": 500.0, "transactions": []}
}

def authenticate(username, password):
    user = users_db.get(username)
    if user and user["password"] == password:
        return user
    return None
