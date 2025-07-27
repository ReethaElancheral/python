class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.current_room = None

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def is_alive(self):
        return self.health > 0
