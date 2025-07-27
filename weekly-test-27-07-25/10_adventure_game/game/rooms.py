class Room:
    def __init__(self, name, description, enemies=None, items=None, connections=None):
        self.name = name
        self.description = description
        self.enemies = enemies if enemies else []
        self.items = items if items else []
        self.connections = connections if connections else {} 

    def connect(self, direction, room):
        self.connections[direction] = room

    def get_connection(self, direction):
        return self.connections.get(direction)
