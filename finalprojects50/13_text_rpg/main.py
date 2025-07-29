# 13. Text-Based RPG (Adventure Game) 
# Objective: Navigate through a story with choices. 
# Requirements: 
#  OOP: Player (health, inventory), Scene (description, choices). 
#  Dictionary: Store scenes (key: scene ID, value: Scene object). 
#  File Handling: Save/load game state. 
#  Exception Handling: Invalid choice input. 
#  Functions: Move between scenes, fight enemies. 
#  Conditionals: Different outcomes based on choices. 
#  Loops: Main game loop. 
#  List: Player inventory. 
#  Generator: Yield loot drops. 
#  Decorator: @save_progress after each move.


from rpg.core import Game

def main():
    print("🗡️ Welcome to the Text-Based RPG Adventure Game!")

    game = Game()

    while True:
        scene = game.get_current_scene()
        if not scene:
            print("⚠️ Scene data missing.")
            break

        print(f"\n{scene.description}")
        if not scene.choices:
            print("🏆 Game Over.")
            break

        game.display_choices()
        choice = input("Choose your action (number) or type 'exit' to quit: ").strip().lower()

        if choice in ("exit", "q"):
            print("👋 Thanks for playing! Goodbye!")
            break

        if not choice.isdigit():
            print("⚠️ Invalid input, please enter a number or 'exit'.")
            continue

        choice_index = int(choice) - 1
        choice_key = game.get_choice_key(choice_index)
        if not choice_key:
            print("⚠️ Invalid choice number.")
            continue

        alive = game.move_to_scene(choice_key)
        if not alive or not game.player.is_alive():
            print("💀 You have died. Game Over.")
            break

if __name__ == "__main__":
    main()


from rpg.core import Game

def main():
    print("🗡️ Welcome to the Text-Based RPG Adventure Game!")

    game = Game()

    while True:
        scene = game.get_current_scene()
        if not scene:
            print("⚠️ Scene data missing.")
            break

        print(f"\n{scene.description}")
        if not scene.choices:
            print("🏆 Game Over.")
            break

        game.display_choices()
        choice = input("Choose your action (number) or type 'exit' to quit: ").strip().lower()

        if choice in ("exit", "q"):
            print("👋 Thanks for playing! Goodbye!")
            break

        if not choice.isdigit():
            print("⚠️ Invalid input, please enter a number or 'exit'.")
            continue

        choice_index = int(choice) - 1
        choice_key = game.get_choice_key(choice_index)
        if not choice_key:
            print("⚠️ Invalid choice number.")
            continue

        alive = game.move_to_scene(choice_key)
        if not alive or not game.player.is_alive():
            print("💀 You have died. Game Over.")
            break

if __name__ == "__main__":
    main()
