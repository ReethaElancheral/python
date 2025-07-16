# 2. Email Duplicate Remover

# Goal: Remove duplicate emails from a contact import.
# Requirements:
# - Import contacts from a list (with duplicates).
# - Convert to a set to remove duplicates.
# - Export the cleaned set to a list.
# - Check if certain email is present using in.
# Concepts Covered: Set creation, in, list-to-set conversion.


raw_contacts = [
    "alice@example.com", "bob@example.com", "alice@example.com",
    "carol@example.com", "bob@example.com"
]
print("Raw contacts:", raw_contacts)


unique_set = set(raw_contacts)
print("Unique email set:", unique_set)


cleaned_contacts = list(unique_set)
print("Cleaned contacts list:", cleaned_contacts)


for email in ["alice@example.com", "dan@example.com"]:
    print(f"Is {email} present?", email in unique_set)
