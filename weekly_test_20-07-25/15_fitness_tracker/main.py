from fitness.tracker import add_activity, edit_activity
from fitness.stats import view_stats, group_by_type, list_unique_activities

activities = []

if __name__ == "__main__":
   
    add_activity(activities, "2025-07-18", "Running", 30, 300)
    add_activity(activities, "2025-07-19", "Cycling", 45, 400)
    add_activity(activities, "2025-07-19", "Yoga", 60, 200)

    print("\nGrouped by type:")
    print(group_by_type(activities))

    print("\nUnique activities:")
    print(list_unique_activities(activities))

    print("\nEditing activity...")
    edit_activity(activities, 1, duration=50, calories=420)

    print("\nStats:")
    view_stats(activities, goal_calories=1000)
