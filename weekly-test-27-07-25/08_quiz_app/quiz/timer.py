import threading

class QuizTimer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.time_up = False

    def start(self):
        timer = threading.Timer(self.seconds, self._time_out)
        timer.start()

    def _time_out(self):
        self.time_up = True
        print("\nTime's up!")
