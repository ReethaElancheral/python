import datetime
import time
from playsound import playsound
from functools import wraps

def snooze(func):
    """Decorator to add snooze delay before alarm plays."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        delay = kwargs.get('delay', 5)  # default 5 seconds snooze
        print(f"⏳ Snoozing for {delay} seconds...")
        time.sleep(delay)
        return func(*args, **kwargs)
    return wrapper

class AlarmClock:
    def __init__(self, alarm_sound_path):
        self.alarm_sound_path = alarm_sound_path

    def validate_time(self, time_str):
        """Validate time format HH:MM (24-hour)."""
        try:
            valid_time = datetime.datetime.strptime(time_str, "%H:%M").time()
            return valid_time
        except ValueError:
            raise ValueError("Invalid time format. Use HH:MM (24-hour).")

    def set_alarm(self, alarm_time_str):
        alarm_time = self.validate_time(alarm_time_str)
        print(f"⏰ Alarm set for {alarm_time_str}. Waiting...")

        while True:
            now = datetime.datetime.now().time()
            if now >= alarm_time:
                self.play_alarm()
                break
            time.sleep(10)  # Check every 10 seconds

    @snooze
    def play_alarm(self, delay=0):
        print("🔔 Alarm ringing!")
        playsound(self.alarm_sound_path)
