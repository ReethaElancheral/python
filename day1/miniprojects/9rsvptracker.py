## 9. Event RSVP Tracker


# - Ask for the names of three attendees (input).
# - Store in a set to avoid duplicates.
# - Print the set and its type.

attendee1 = input("Enter the name of attendee 1: ")
attendee2 = input("Enter the name of attendee 2: ")
attendee3 = input("Enter the name of attendee 3: ")


attendees = {attendee1, attendee2, attendee3}

print("Attendees:", attendees)
print("Type of attendees variable:", type(attendees))
