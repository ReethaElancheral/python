import random
from .player import Player
from .rooms import Room

def combat(player, enemy):
    print(f"Combat started: You vs {enemy['name']} (Health: {enemy['health']})")
    while player.is_alive() and enemy["health"] > 0:
        action = input("Attack (a) or Run (r)? ").lower()
        if action == "a":
            damage = random.randint(10, 25)
            enemy["health"] -= damage
            print(f"You hit {enemy['name']} for {damage} damage!")
            if enemy["health"] <= 0:
                print(f"{enemy['name']} defeated!")
                return True
            # Enemy attacks back
            edamage = random.randint(5, 20)
            player.health -= edamage
            print(f"{enemy['name']} hits you for {edamage} damage! Your health: {player.health}")
            if not player.is_alive():
                print("You have been defeated...")
                return False
        elif action == "r":
            print("You fled the combat.")
            return False
        else:
            print("Invalid action.")
    return player.is_alive()

def game_loop(player, rooms):
    while True:
        room = player.current_room
        print(f"\nYou are in {room.name}.")
        print(room.description)

        # Show items
        if room.items:
            print("You see the following items:")
            for item in room.items:
                print(f"- {item}")

        # Show enemies
        if room.enemies:
            print("Enemies here:")
            for enemy in room.enemies:
                print(f"- {enemy['name']} (Health: {enemy['health']})")

        print("\nInventory:", player.inventory)
        print("Health:", player.health)

        cmd = input("\nEnter command (move, take, fight, save, load, quit): ").lower()

        if cmd == "move":
            direction = input("Direction (north, south, east, west): ").lower()
            next_room = room.get_connection(direction)
            if next_room:
                player.current_room = next_room
            else:
                print("You can't go that way.")

        elif cmd == "take":
            if room.items:
                item = input("Enter item name to take: ")
                if item in room.items:
                    player.add_item(item)
                    room.items.remove(item)
                    print(f"{item} added to your inventory.")
                else:
                    print("Item not found.")
            else:
                print("No items here.")

        elif cmd == "fight":
            if room.enemies:
                enemy = room.enemies[0]
                won = combat(player, enemy)
                if won:
                    room.enemies.remove(enemy)
                    # Check for ending or rewards here
                else:
                    print("Game Over.")
                    break
            else:
                print("No enemies to fight.")

        elif cmd == "save":
            from .save_load import save_game
            save_game(player)

        elif cmd == "load":
            from .save_load import load_game
            loaded_player = load_game(rooms)
            if loaded_player:
                player = loaded_player

        elif cmd == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Unknown command.")
