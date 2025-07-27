def add_contact(contacts, name, phone, email, category):
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    }
    contacts.append(contact)

def delete_contact(contacts, name):
    contacts[:] = [c for c in contacts if c["name"].lower() != name.lower()]

def edit_contact(contacts, name, new_name=None, new_phone=None, new_email=None, new_category=None):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_category:
                contact["category"] = new_category
            break

def search_contacts(contacts, keyword):
    keyword = keyword.lower()
    return [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]

def group_contacts(contacts):
    grouped = {}
    for contact in contacts:
        category = contact["category"]
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(contact)
    return grouped

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} | {c['phone']} | {c['email']} | Category: {c['category']}")
