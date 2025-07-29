from alarm.core import AlarmClock

def main():
    print("⏰ Welcome to CLI Alarm Clock")

    alarm_sound = "alarm_sound.mp3"  # Place your mp3 file in the folder
    alarm = AlarmClock(alarm_sound)

    while True:
        time_input = input("Set alarm time (HH:MM 24-hour) or 'exit' to quit: ").strip()
        if time_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            alarm.set_alarm(time_input)
        except ValueError as ve:
            print(f"❌ {ve}")

if __name__ == "__main__":
    main()
