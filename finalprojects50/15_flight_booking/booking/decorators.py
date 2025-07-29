def confirm_booking(func):
    def wrapper(self, *args, **kwargs):
        confirm = input("Confirm booking? (yes/no): ").strip().lower()
        if confirm == 'yes':
            return func(self, *args, **kwargs)
        else:
            print("Booking cancelled.")
            return False
    return wrapper
