# 19. City Distance Map

# Description: Store distances between cities.
# Requirements:
# - Nested format: {city1: {city2: distance}}
# - Query distance between two cities
# - Update distances
# - Find shortest route using min value


city_distances = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "C": 3},
    "C": {"A": 10, "B": 3, "D": 7},
    "D": {"C": 7}
}

def add_or_update_distance(city1, city2, distance):
 
    city_distances.setdefault(city1, {})[city2] = distance
    city_distances.setdefault(city2, {})[city1] = distance
    print(f"Distance set: {city1} ↔ {city2} = {distance} km")

def query_distance(city1, city2):

    dist = city_distances.get(city1, {}).get(city2)
    if dist is not None:
        print(f"Distance {city1} → {city2}: {dist} km")
        return dist
    else:
        print(f"No direct distance found between {city1} and {city2}")
        return None

def shortest_direct_route(city):
   
    neighbors = city_distances.get(city, {})
    if not neighbors:
        print(f"No routes from {city}")
        return None
    nearest = min(neighbors.items(), key=lambda kv: kv[1])
    print(f"Closest city to {city} is {nearest[0]} at {nearest[1]} km")
    return nearest


add_or_update_distance("D", "E", 2)
query_distance("A", "C")
query_distance("A", "D")
shortest_direct_route("C")
