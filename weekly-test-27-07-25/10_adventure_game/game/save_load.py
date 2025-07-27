import json
from .player import Player


def save_game(player, filename="savegame.json"):
    data = {
        "health": player.health,
        "inventory": player.inventory,
        "current_room": player.current_room.name,
    }
    with open(filename, "w") as f:
        json.dump(data, f)
    print("Game saved.")

def load_game(rooms, filename="savegame.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        player = Player()
        player.health = data["health"]
        player.inventory = data["inventory"]
        player.current_room = rooms.get(data["current_room"])
        print("Game loaded.")
        return player
    except FileNotFoundError:
        print("No saved game found.")
        return None
