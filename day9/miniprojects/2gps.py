# 2. GPS Location Logger

# Goal: Track locations using latitude and longitude stored in tuples.
# Requirements:
# Store GPS coordinates as (latitude, longitude) tuples.
# Maintain a list of these tuples to simulate movement.
# Use slicing to retrieve the last 5 locations.
# Unpack coordinates for mapping on screen.
# Prevent editing the original GPS points.


path = []

path.append((25.276987, 55.296249))  
path.append((25.277500, 55.296800))
path.append((25.278000, 55.297300))
path.append((25.278500, 55.297800))
path.append((25.279000, 55.298300))
path.append((25.279500, 55.298800))
path.append((25.280000, 55.299300))

last_five = path[-5:]
print("📍 Last 5 logged GPS points:")
for i, (lat, lon) in enumerate(last_five, 1):
 
    print(f"{i}. Latitude: {lat}, Longitude: {lon}")


print(f"\nTotal points logged: {len(path)} (immutable tuple data)")
