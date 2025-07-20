from manager.generator import generate_password

def add_account(accounts):
    site = input("Site name: ")
    username = input("Username: ")
    auto_generate = input("Auto-generate password? (y/n): ").lower()
    password = generate_password() if auto_generate == 'y' else input("Password: ")
    tags = set(input("Tags (comma-separated): ").split(','))

    accounts[site] = ((username, password), tags)
    print("Account added.")

def update_account(accounts):
    site = input("Site name to update: ")
    if site in accounts:
        username = input("New username: ")
        password = input("New password: ")
        tags = set(input("New tags (comma-separated): ").split(','))
        accounts[site] = ((username, password), tags)
        print("Account updated.")
    else:
        print("Site not found.")

def delete_account(accounts):
    site = input("Site to delete: ")
    if site in accounts:
        del accounts[site]
        print("Account deleted.")
    else:
        print("Site not found.")

def search_account(accounts):
    key = input("Search by site or tag: ").lower()
    found = False
    for site, ((username, password), tags) in accounts.items():
        if key in site.lower() or key in [tag.lower() for tag in tags]:
            print(f"\nSite: {site}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"Tags: {', '.join(tags)}")
            found = True
    if not found:
        print("No matching accounts found.")

def list_accounts(accounts):
    if not accounts:
        print("No accounts stored.")
    for site in sorted(accounts):
        username, _ = accounts[site][0]
        print(f"{site} → Username: {username}")
