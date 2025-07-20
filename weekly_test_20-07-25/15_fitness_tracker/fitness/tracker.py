def add_activity(activity_list, date, activity_type, duration, calories):
    activity = {
        "date": date,
        "type": activity_type,
        "duration": duration,  # in minutes
        "calories": calories
    }
    activity_list.append(activity)
    print(f"Added activity: {activity_type} on {date}")

def edit_activity(activity_list, index, **updates):
    if 0 <= index < len(activity_list):
        activity_list[index].update(updates)
        print("Activity updated.")
    else:
        print("Invalid activity index.")
