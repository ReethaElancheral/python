# ✅ 17. Simple Hotel Room Booking

# Objective: Calculate room price based on room type.
# Requirements:
# Use dictionary: room type → price.
# Input: room type, nights.
# Calculate total.
# If nights > 3, give 10% off.

room_prices = {
    "single": 1000,
    "double": 1800,
    "suite": 3000
}

room_type = input("Enter room type (single/double/suite): ").lower().strip()
nights = int(input("Enter number of nights: "))

if room_type in room_prices:
    price_per_night = room_prices[room_type]
    total = price_per_night * nights

    if nights > 3:
        discount = total * 0.10
        total -= discount
        print(f"10% discount applied: ₹{discount:.2f}")

    print(f"Total price for {nights} night(s) in a {room_type} room: ₹{total:.2f}")
else:
    print("Invalid room type entered.")
