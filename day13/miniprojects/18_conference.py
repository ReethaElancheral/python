# 18. Conference Registration System

# Concepts: Class, Object, Aggregation, @classmethod
# Classes:  Attendee,  Event, Session, Registration
# Requirements:
# Register attendees, assign sessions
# Use classmethod to view total attendees

class Attendee:
    def __init__(self, attendee_id, name):
        self.attendee_id = attendee_id
        self.name = name

    def __str__(self):
        return f"Attendee: {self.name} (ID: {self.attendee_id})"

class Session:
    def __init__(self, session_id, title):
        self.session_id = session_id
        self.title = title

    def __str__(self):
        return f"Session: {self.title} (ID: {self.session_id})"

class Event:
    def __init__(self, event_name):
        self.event_name = event_name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)
        print(f"Session '{session.title}' added to event '{self.event_name}'.")

    def __str__(self):
        session_titles = ', '.join(session.title for session in self.sessions)
        return f"Event: {self.event_name} with sessions: {session_titles}"

class Registration:
    total_attendees = 0

    def __init__(self, attendee, event):
        self.attendee = attendee
        self.event = event
        self.sessions_registered = []
        Registration.total_attendees += 1

    def register_session(self, session):
        if session in self.event.sessions:
            self.sessions_registered.append(session)
            print(f"{self.attendee.name} registered for session '{session.title}'.")
        else:
            print(f"Session '{session.title}' is not part of the event '{self.event.event_name}'.")

    @classmethod
    def view_total_attendees(cls):
        print(f"Total attendees registered: {cls.total_attendees}")

    def __str__(self):
        sessions = ', '.join(session.title for session in self.sessions_registered) or "No sessions registered"
        return (f"Registration: {self.attendee.name} for event '{self.event.event_name}'\n"
                f"Sessions: {sessions}")

def main():
    # Create event and sessions
    event = Event("Tech Conference 2025")
    session1 = Session(1, "AI and Machine Learning")
    session2 = Session(2, "Cybersecurity Essentials")
    session3 = Session(3, "Cloud Computing")

    event.add_session(session1)
    event.add_session(session2)
    event.add_session(session3)

    # Create attendees
    attendee1 = Attendee(101, "Nisha")
    attendee2 = Attendee(102, "Ravi")

    # Registrations
    reg1 = Registration(attendee1, event)
    reg1.register_session(session1)
    reg1.register_session(session3)

    reg2 = Registration(attendee2, event)
    reg2.register_session(session2)

    # View total attendees
    Registration.view_total_attendees()

    # Print registration info
    print()
    print(reg1)
    print(reg2)

if __name__ == "__main__":
    main()
