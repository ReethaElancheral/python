# 14. IP Logger with Blacklist

# Goal: Log only clean IPs from visitors.
# Requirements:
# - Store visitor IPs in a set.
# - Store blacklist in another set.
# - Use isdisjoint() to validate before adding.
# - If blacklisted, discard() or skip.
# Concepts Covered: isdisjoint(), discard(), membership test.

# Set of blacklisted IPs
blacklist = {"192.168.1.100", "10.0.0.5", "203.0.113.7"}

# Set to store clean visitor IPs
visitor_ips = set()

# Function to log a visitor IP
def log_ip(ip):
    if blacklist.isdisjoint({ip}):
        visitor_ips.add(ip)
        print(f"IP {ip} logged successfully.")
    else:
        print(f"IP {ip} is blacklisted and cannot be logged.")

# Test the function
log_ip("192.168.1.101")  # Clean IP
log_ip("192.168.1.100")  # Blacklisted IP

# Display all logged visitor IPs
print("Logged visitor IPs:", visitor_ips)
