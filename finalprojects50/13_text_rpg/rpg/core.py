import json
import random
from .decorators import save_progress

class Player:
    def __init__(self, health=100, inventory=None):
        self.health = health
        self.inventory = inventory if inventory else []

    def is_alive(self):
        return self.health > 0

    def add_loot(self, loot):
        self.inventory.append(loot)

    def __str__(self):
        inv = ', '.join(self.inventory) if self.inventory else "Empty"
        return f"Health: {self.health}\nInventory: {inv}"

class Scene:
    def __init__(self, scene_id, description, choices, enemy=None, loot=None):
        self.scene_id = scene_id
        self.description = description
        self.choices = choices  # dict of choice_text: next_scene_id
        self.enemy = enemy      # None or dict with enemy info {name, damage}
        self.loot = loot        # None or string loot name

    def has_enemy(self):
        return self.enemy is not None

class Game:
    def __init__(self, scenes_file="rpg/scenes.json", save_file="rpg/game_state.json"):
        self.scenes_file = scenes_file
        self.save_file = save_file
        self.player = Player()
        self.current_scene_id = "start"
        self.scenes = self.load_scenes()
        self.load_game()

    def load_scenes(self):
        try:
            with open(self.scenes_file, 'r') as f:
                data = json.load(f)
            scenes = {}
            for sid, info in data.items():
                scenes[sid] = Scene(
                    scene_id=sid,
                    description=info["description"],
                    choices=info["choices"],
                    enemy=info.get("enemy"),
                    loot=info.get("loot")
                )
            return scenes
        except FileNotFoundError:
            print("⚠️ Scenes file not found.")
            return {}

    def save_game(self):
        data = {
            "health": self.player.health,
            "inventory": self.player.inventory,
            "current_scene_id": self.current_scene_id
        }
        with open(self.save_file, 'w') as f:
            json.dump(data, f)

    def load_game(self):
        try:
            with open(self.save_file, 'r') as f:
                data = json.load(f)
                self.player.health = data.get("health", 100)
                self.player.inventory = data.get("inventory", [])
                self.current_scene_id = data.get("current_scene_id", "start")
        except FileNotFoundError:
            pass

    def fight_enemy(self, enemy):
        print(f"⚔️ You encountered an enemy: {enemy['name']}!")
        # Simple fight: player and enemy exchange damage until player loses health
        enemy_damage = enemy.get("damage", 10)
        # Player attacks first
        enemy_defeated = False
        while self.player.is_alive() and not enemy_defeated:
            # Player attack chance: 70%
            if random.random() < 0.7:
                print(f"💥 You hit the {enemy['name']}!")
                enemy_defeated = True
                print(f"🎉 You defeated the {enemy['name']}!")
            else:
                print(f"❌ You missed!")
            if not enemy_defeated:
                self.player.health -= enemy_damage
                print(f"😵 {enemy['name']} hit you for {enemy_damage} damage! Your health: {self.player.health}")
        if not self.player.is_alive():
            print("💀 You have been defeated...")
        return enemy_defeated and self.player.is_alive()

    def loot_generator(self, loot):
        # Simple generator yields loot item once
        yield loot

    @save_progress
    def move_to_scene(self, choice_key):
        current_scene = self.scenes.get(self.current_scene_id)
        if not current_scene:
            print("⚠️ Current scene not found!")
            return False

        next_scene_id = current_scene.choices.get(choice_key)
        if not next_scene_id:
            print("⚠️ Invalid choice!")
            return False

        self.current_scene_id = next_scene_id
        next_scene = self.scenes.get(next_scene_id)

        print(f"\n🌄 {next_scene.description}")

        if next_scene.has_enemy():
            survived = self.fight_enemy(next_scene.enemy)
            if not survived:
                return False

        if next_scene.loot:
            for item in self.loot_generator(next_scene.loot):
                self.player.add_loot(item)
                print(f"🎁 You found loot: {item}")

        return True

    def get_current_scene(self):
        return self.scenes.get(self.current_scene_id)

    def display_choices(self):
        scene = self.get_current_scene()
        if not scene:
            print("⚠️ Scene not found.")
            return
        print("\nChoices:")
        for idx, (desc, _) in enumerate(scene.choices.items(), 1):
            print(f"{idx}. {desc}")

    def get_choice_key(self, index):
        scene = self.get_current_scene()
        if not scene:
            return None
        keys = list(scene.choices.keys())
        if 0 <= index < len(keys):
            return keys[index]
        return None
