# 13. User Authentication Middleware (Simulated) 
# Objective: Only allow function access if user is authenticated. 
# Requirements: 
#  Use @require_login decorator 
#  Simulate user["is_logged_in"] = True 
#  Block and raise exception if not authenticated 

from functools import wraps

def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in", False):
            raise PermissionError("User not authenticated.")
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_dashboard(user):
    print(f"Welcome, {user['name']}! Here's your dashboard.")

# Example:
user1 = {"name": "Nisha", "is_logged_in": True}
view_dashboard(user1)

# user2 = {"name": "Reetha", "is_logged_in": False}
# view_dashboard(user2)  # Raises PermissionError
