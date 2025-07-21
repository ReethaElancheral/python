# 9. Gym Membership Management

# Concepts: Class, Inheritance, Class Variables, Overloading
# Classes:  Member, Trainer, Schedule,  Subscription
# Requirements:
# Book slots, assign trainer
# Use *args to register for multiple sessions
# Use class variable to track total members

class Member:
    total_members = 0  # class variable to track total members

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.sessions = []
        Member.total_members += 1

    def book_sessions(self, *session_names):
        for session in session_names:
            self.sessions.append(session)
            print(f"{self.name} booked session: {session}")

    def __str__(self):
        sessions = ', '.join(self.sessions) if self.sessions else "No sessions booked"
        return f"Member {self.name} (ID: {self.member_id}), Sessions: {sessions}"

    @classmethod
    def get_total_members(cls):
        return cls.total_members

class Trainer:
    def __init__(self, trainer_id, name, specialty):
        self.trainer_id = trainer_id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Trainer {self.name} (ID: {self.trainer_id}), Specialty: {self.specialty}"

class Schedule:
    def __init__(self):
        self.bookings = {}  # session_name -> list of members

    def assign_trainer(self, session_name, trainer):
        print(f"Trainer {trainer.name} assigned to session {session_name}")

    def book_slot(self, member, session_name):
        if session_name not in self.bookings:
            self.bookings[session_name] = []
        self.bookings[session_name].append(member)
        member.book_sessions(session_name)
        print(f"Slot booked for {member.name} in session '{session_name}'")

class Subscription:
    def __init__(self, member, plan_name, duration_months):
        self.member = member
        self.plan_name = plan_name
        self.duration_months = duration_months

    def __str__(self):
        return (f"Subscription for {self.member.name}: Plan {self.plan_name}, "
                f"Duration: {self.duration_months} month(s)")

def main():
    # Create members
    member1 = Member(101, "Nisha")
    member2 = Member(102, "Rajesh")

    # Create trainers
    trainer1 = Trainer(201, "Alice", "Yoga")
    trainer2 = Trainer(202, "Bob", "Weightlifting")

    # Create schedule
    schedule = Schedule()

    # Assign trainers to sessions
    schedule.assign_trainer("Morning Yoga", trainer1)
    schedule.assign_trainer("Evening Weightlifting", trainer2)

    # Members book multiple sessions
    schedule.book_slot(member1, "Morning Yoga")
    schedule.book_slot(member1, "Evening Weightlifting")
    schedule.book_slot(member2, "Morning Yoga")

    # Show member details
    print(member1)
    print(member2)

    # Show total members
    print(f"Total gym members: {Member.get_total_members()}")

    # Create subscriptions
    sub1 = Subscription(member1, "Premium", 6)
    sub2 = Subscription(member2, "Basic", 3)

    print(sub1)
    print(sub2)

if __name__ == "__main__":
    main()
