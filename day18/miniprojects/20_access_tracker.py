# 20. Access Tracker for Sensitive Data 
# Objective: Track access to secure data using property decorators. 
# Requirements: 
#  Use @property to define secure data access 
#  Log every time property is read 
#  Deny write access with error 

class SecureData:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        print("[ACCESS LOG] Secure data accessed.")
        return self._data

    @data.setter
    def data(self, value):
        raise PermissionError("Write access denied to secure data.")

# Example usage:
obj = SecureData("Secret123")
print(obj.data)
# obj.data = "NewSecret"  # Raises error
