from controller.traffic_control import activate_signal, deactivate_signal, view_active_signals

def main():
    signals = {}         
    active_signals = set()

    while True:
        print("\nTraffic Signal Controller")
        print("1. Activate Signal")
        print("2. Deactivate Signal")
        print("3. View Active Signals")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            location = input("Enter location: ").strip()
            time = input("Enter time (e.g. 08:00AM): ").strip()
            status = input("Enter status (RED/YELLOW/GREEN): ").strip().upper()

            activate_signal(signals, active_signals, location, time, status)

        elif choice == "2":
            location = input("Enter location: ").strip()
            time = input("Enter time: ").strip()

            deactivate_signal(signals, active_signals, location, time)

        elif choice == "3":
            view_active_signals(signals, active_signals)

        elif choice == "4":
            print("Exiting Traffic Controller.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
