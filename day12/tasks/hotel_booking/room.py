_rooms = {}

def add_room(room_id, info):
    _rooms[room_id] = info
def get_room(room_id):
    return _rooms.get(room_id)
