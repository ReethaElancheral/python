import time
from functools import wraps

def notify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\n⏰ Timer complete! Take a break or start another session.")
        return result
    return wrapper

class PomodoroTimer:
    def __init__(self, work_minutes=25, short_break=5, long_break=15, cycles=4):
        self.work_minutes = work_minutes
        self.short_break = short_break
        self.long_break = long_break
        self.cycles = cycles

    def generator_timer(self, seconds):
        for remaining in range(seconds, 0, -1):
            yield remaining
            time.sleep(1)

    @notify
    def start_work(self):
        print(f"Starting work session for {self.work_minutes} minutes.")
        for sec in self.generator_timer(self.work_minutes * 60):
            mins, secs = divmod(sec, 60)
            print(f"Work Time Left: {mins:02d}:{secs:02d}", end="\r")
        print()

    def start_short_break(self):
        print(f"Starting short break for {self.short_break} minutes.")
        for sec in self.generator_timer(self.short_break * 60):
            mins, secs = divmod(sec, 60)
            print(f"Break Time Left: {mins:02d}:{secs:02d}", end="\r")
        print()

    def start_long_break(self):
        print(f"Starting long break for {self.long_break} minutes.")
        for sec in self.generator_timer(self.long_break * 60):
            mins, secs = divmod(sec, 60)
            print(f"Long Break Left: {mins:02d}:{secs:02d}", end="\r")
        print()

    def run(self):
        print("Pomodoro Timer Started. Press Ctrl+C to stop anytime.\n")
        try:
            for cycle in range(1, self.cycles + 1):
                print(f"Cycle {cycle} of {self.cycles}")
                self.start_work()
                if cycle < self.cycles:
                    self.start_short_break()
                else:
                    self.start_long_break()
            print("Pomodoro cycles complete! Great job!")
        except KeyboardInterrupt:
            print("\nTimer interrupted by user. Exiting...")

def main():
    timer = PomodoroTimer()
    timer.run()

if __name__ == "__main__":
    main()

