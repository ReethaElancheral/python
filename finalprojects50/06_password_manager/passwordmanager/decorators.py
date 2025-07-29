# passwordmanager/decorators.py

def logged_in(func):
    def wrapper(self, *args, **kwargs):
        if not getattr(self, "authenticated", False):
            print("❌ You must log in first.")
            return
        return func(self, *args, **kwargs)
    return wrapper
