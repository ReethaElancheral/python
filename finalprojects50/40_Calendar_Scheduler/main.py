import json
from datetime import datetime, time
from functools import wraps

CALENDAR_FILE = "calendar.json"

def save_calendar(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.save()
        return result
    return wrapper

class Event:
    def __init__(self, title, date_str, start_time_str, end_time_str):
        self.title = title
        self.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        self.start_time = datetime.strptime(start_time_str, "%H:%M").time()
        self.end_time = datetime.strptime(end_time_str, "%H:%M").time()
        if self.end_time <= self.start_time:
            raise ValueError("End time must be after start time")

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date.isoformat(),
            "start_time": self.start_time.strftime("%H:%M"),
            "end_time": self.end_time.strftime("%H:%M"),
        }

    def __str__(self):
        return f"{self.title}: {self.date} {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

class CalendarScheduler:
    def __init__(self):
        self.events = {}  # date string -> list of Event objects
        self.load()

    def load(self):
        try:
            with open(CALENDAR_FILE, "r") as f:
                data = json.load(f)
            for date_str, events_list in data.items():
                self.events[date_str] = [Event(**event) for event in events_list]
        except (FileNotFoundError, json.JSONDecodeError):
            self.events = {}

    def save(self):
        data = {}
        for date_str, events_list in self.events.items():
            data[date_str] = [event.to_dict() for event in events_list]
        with open(CALENDAR_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def list_events(self, date_str):
        if date_str not in self.events or not self.events[date_str]:
            print("No events for this date.")
            return
        for event in sorted(self.events[date_str], key=lambda e: e.start_time):
            print(event)

    def check_conflict(self, date_str, new_event):
        if date_str not in self.events:
            return False
        for event in self.events[date_str]:
            # Check if times overlap
            if not (new_event.end_time <= event.start_time or new_event.start_time >= event.end_time):
                return True
        return False

    @save_calendar
    def add_event(self, title, date_str, start_time_str, end_time_str):
        try:
            new_event = Event(title, date_str, start_time_str, end_time_str)
        except ValueError as e:
            print(f"Error: {e}")
            return
        if self.check_conflict(date_str, new_event):
            print("Time conflict detected! Event not added.")
            return
        self.events.setdefault(date_str, []).append(new_event)
        print("Event added successfully.")

    @save_calendar
    def remove_event(self, date_str, title):
        if date_str not in self.events:
            print("No events on this date.")
            return
        initial_count = len(self.events[date_str])
        self.events[date_str] = [e for e in self.events[date_str] if e.title.lower() != title.lower()]
        if len(self.events[date_str]) < initial_count:
            print("Event removed.")
            if not self.events[date_str]:
                del self.events[date_str]
        else:
            print("Event not found.")

    def generator_daily_events(self, date_str):
        if date_str in self.events:
            for event in sorted(self.events[date_str], key=lambda e: e.start_time):
                yield event

def main():
    scheduler = CalendarScheduler()

    print("Calendar Scheduler CLI")
    while True:
        print("\nOptions:\n1. Add event\n2. Remove event\n3. List events by date\n4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            title = input("Event title: ").strip()
            date_str = input("Date (YYYY-MM-DD): ").strip()
            start_time = input("Start time (HH:MM 24h): ").strip()
            end_time = input("End time (HH:MM 24h): ").strip()
            scheduler.add_event(title, date_str, start_time, end_time)
        elif choice == '2':
            date_str = input("Date of event to remove (YYYY-MM-DD): ").strip()
            title = input("Event title to remove: ").strip()
            scheduler.remove_event(date_str, title)
        elif choice == '3':
            date_str = input("Date to list events (YYYY-MM-DD): ").strip()
            print(f"Events on {date_str}:")
            for event in scheduler.generator_daily_events(date_str):
                print(event)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

