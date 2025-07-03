# 10. Access Control Based on Role

# Objective: Grant access based on user role and ID.
# Requirements:
# Input: role (admin/user), has_id (yes/no).
# Use nested if.
# Use and, not, and membership operator (in) to validate.

role = input("Enter your role (admin/user): ").lower()
has_id = input("Do you have an ID? (yes/no): ").lower()

allowed_roles = ["admin", "user"]

if role in allowed_roles:
    if has_id == "yes" and not role == "user":
        print("Access granted: Admin with ID.")
    elif has_id == "yes" and role == "user":
        print("Access granted: User with ID.")
    else:
        print("Access denied: ID required.")
else:
    print("Access denied: Invalid role.")
