# 19. System Permissions Audit

# Goal: Check if users have all required access.
# Requirements:
# - Store required permissions in a set.
# - Use issubset() to validate user permission sets.
# - Output missing permissions with difference().
# Concepts Covered: issubset(), difference().

# Define required permissions
required_permissions = {"read", "write", "execute"}

# Define user permissions
user_permissions = {"read", "write"}

# Check if user has all required permissions
if user_permissions.issubset(required_permissions):
    print("User has all required permissions.")
else:
    # Find missing permissions
    missing_permissions = required_permissions.difference(user_permissions)
    print("Missing permissions:", missing_permissions)
