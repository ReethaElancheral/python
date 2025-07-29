import functools

def admin_only(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not getattr(self, 'is_admin', False):
            print("⚠️ Access denied: Admins only!")
            return None
        return func(self, *args, **kwargs)
    return wrapper
