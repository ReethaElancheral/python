## 2. Simple Contact Book

# - Ask the user for their name, phone, and email.
# - Store these in a dictionary.
# - Print the contact information with labels.
# - Display the type of each value using type().

name = input("Enter Your Name:")
phone = int(input("Enter your Phone Number"))
email = input("Enter you Email id:")

contact = {
           "Name":name,
           "Phone": phone,
           "Email": email
           }

print("\n Contact Information:")
print(f"Name: {contact['Name']}")
print(f"Phone: {contact['Phone']}")
print(f"Email: {contact['Email']}")


print("\nData Types:")
print("Name:", type(contact["Name"]))
print("Phone:", type(contact["Phone"]))
print("Email:", type(contact["Email"]))