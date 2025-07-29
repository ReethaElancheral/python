def admin_only(func):
    def wrapper(*args, **kwargs):
        password = input("Enter admin password to proceed: ")
        if password == "1234":
            return func(*args, **kwargs)
        else:
            print("❌ Access denied. Admin privileges required.")
    return wrapper
