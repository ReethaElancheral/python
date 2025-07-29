import subprocess
import re

def get_saved_wifi_passwords():
    # Get list of WiFi profiles
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    profiles = re.findall(r"All User Profile\s*:\s(.*)", result.stdout)
    
    wifi_passwords = {}
    for profile in profiles:
        profile = profile.strip()
        # Get the password for each profile
        cmd = ["netsh", "wlan", "show", "profile", profile, "key=clear"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        password_search = re.search(r"Key Content\s*:\s(.*)", result.stdout)
        password = password_search.group(1) if password_search else "No password found"
        wifi_passwords[profile] = password
    return wifi_passwords

def main():
    print("WiFi Password Viewer (Windows Only)")
    wifi_passwords = get_saved_wifi_passwords()
    if not wifi_passwords:
        print("No WiFi profiles found.")
        return
    for ssid, password in wifi_passwords.items():
        print(f"SSID: {ssid}\nPassword: {password}\n{'-'*30}")

if __name__ == "__main__":
    main()
