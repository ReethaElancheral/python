from collections import defaultdict

def group_by_type(activity_list):
    grouped = defaultdict(list)
    for activity in activity_list:
        grouped[activity["type"]].append(activity)
    return dict(grouped)

def list_unique_activities(activity_list):
    return set(activity["type"] for activity in activity_list)

def view_stats(activity_list, goal_calories=500):
    total_duration = sum(a["duration"] for a in activity_list)
    total_calories = sum(a["calories"] for a in activity_list)

    print(f"Total Duration: {total_duration} minutes")
    print(f"Total Calories Burned: {total_calories} kcal")

    if total_calories >= goal_calories:
        print("🎯 Goal Achieved!")
    else:
        print("Keep going! 💪")
