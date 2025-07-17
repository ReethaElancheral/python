from .room import get_room
from .guests import register_guest

_bookings = []

def book(room_id, guest_name):
    room = get_room(room_id)
    if room:
        register_guest(guest_name)
        _bookings.append({"room": room_id, "guest": guest_name})
        print(f"Booked room {room_id} for {guest_name}")
    else:
        print("Room not found")

def list_bookings():
    return _bookings
