# 1. Unique Visitor Tracker

# Goal: Track unique visitors to a website.
# Requirements:
# - Store each visitor’s IP in a set.
# - Use add() for each new IP.
# - Use len() to get total unique visits.
# - Use discard() to remove blacklisted IPs.
# - Save a backup of visitor set using copy().
# Concepts Covered: add(), discard(), copy(), membership test, len().


visitor_ips = set()


def add_visitor(ip):
    visitor_ips.add(ip)


def remove_blacklisted(ip):
    visitor_ips.discard(ip)


def get_unique_visits():
    return len(visitor_ips)


def backup_visitors():
    return visitor_ips.copy()


add_visitor("192.168.1.1")
add_visitor("192.168.1.2")
add_visitor("192.168.1.3")
add_visitor("192.168.1.1") 


remove_blacklisted("192.168.1.2")


print("Total unique visits:", get_unique_visits())


backup = backup_visitors()
print("Backup of visitor IPs:", backup)
