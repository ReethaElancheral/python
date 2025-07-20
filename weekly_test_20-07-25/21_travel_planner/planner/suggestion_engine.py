def suggest_destinations(trips):
    visited = {trip['destination'] for trip in trips}
    suggestions = {"Paris", "Tokyo", "Cairo", "Sydney", "Reykjavik", "Rome"} - visited

    if suggestions:
        print("Suggested destinations you haven't visited yet:")
        for dest in suggestions:
            print(f"- {dest}")
    else:
        print("You've already visited all recommended destinations!")
