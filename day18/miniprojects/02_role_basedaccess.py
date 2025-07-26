# 2. Role-Based Access Control System 
# Objective: Restrict access to certain functions based on user role. 
# Requirements: 
#  Create a decorator that takes a role as a parameter 
#  Use @access_control("admin") 
#  Block access if user’s role doesn’t match 
#  Log denied access attempts


from functools import wraps
def access_control(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != required_role:
                print(f"Access Denied for user: {user['name']} | Required: {required_role}")
                return
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@access_control("admin")
def delete_user(user, user_id):
    print(f"{user['name']} deleted user {user_id}")

admin = {"name": "Alice", "role": "admin"}
guest = {"name": "Bob", "role": "guest"}

delete_user(admin, 101)
delete_user(guest, 101)
