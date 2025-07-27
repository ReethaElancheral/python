from game.rooms import Room
from game.player import Player
from game.game_engine import game_loop

def setup_game():
    # Create rooms
    foyer = Room("Foyer", "A small entrance hall with dusty furniture.")
    hall = Room("Hall", "A grand hall with portraits on the walls.")
    armory = Room("Armory", "Room filled with old weapons and armor.", enemies=[{"name": "Goblin", "health": 50}])
    treasure_room = Room("Treasure Room", "Glittering with gold and jewels!", items=["Golden Crown"])

    # Connect rooms
    foyer.connect("north", hall)
    hall.connect("south", foyer)
    hall.connect("east", armory)
    armory.connect("west", hall)
    hall.connect("north", treasure_room)
    treasure_room.connect("south", hall)

    rooms = {
        "Foyer": foyer,
        "Hall": hall,
        "Armory": armory,
        "Treasure Room": treasure_room
    }

    player = Player()
    player.current_room = foyer
    return player, rooms

def main():
    player, rooms = setup_game()
    print("Welcome to the Text Adventure Game!")
    game_loop(player, rooms)

if __name__ == "__main__":
    main()
