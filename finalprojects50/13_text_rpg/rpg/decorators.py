import functools
import json

def save_progress(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        try:
            self.save_game()
        except Exception as e:
            print(f"⚠️ Could not save progress: {e}")
        return result
    return wrapper
