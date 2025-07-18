def activate_signal(signals, active_set, location, time, status):
    signal_id = (location, time)

    if signal_id in signals:
        print(f"Signal at {location} during {time} already exists. Updating status.")
    else:
        print(f"Activating new signal at {location} during {time}.")

    signals[signal_id] = status
    active_set.add(signal_id)
    print(f"Status: {status}")

def deactivate_signal(signals, active_set, location, time):
    signal_id = (location, time)

    if signal_id in active_set:
        active_set.remove(signal_id)
        print(f"Deactivated signal at {location} during {time}.")
    else:
        print("Signal is not active.")

def view_active_signals(signals, active_set):
    if not active_set:
        print("No active signals.")
        return

    print("\n--- Active Signals ---")
    for signal_id in active_set:
        status = signals.get(signal_id, "Unknown")
        print(f"Location: {signal_id[0]}, Time: {signal_id[1]}, Status: {status}")
