# 20. Class Schedule Collision Detector

# Goal: Detect conflicting class schedules.
# Requirements:
# - Store class slots as sets.
# - Use intersection() to find conflicts.
# - Suggest available slots using difference().
# Concepts Covered: intersection(), difference(), add().

# Define class schedules as sets of time slots
class_schedule = {
    "Math": {"09:00-10:30", "14:00-15:30"},
    "History": {"10:00-11:30", "15:00-16:30"},
    "Physics": {"09:30-11:00", "13:00-14:30"},
    "Chemistry": {"11:00-12:30", "14:30-16:00"}
}

# Function to detect conflicts between two classes
def detect_conflicts(class1, class2):
    common_slots = class_schedule[class1].intersection(class_schedule[class2])
    if common_slots:
        print(f"Conflict detected between {class1} and {class2}: {common_slots}")
    else:
        print(f"No conflict between {class1} and {class2}")

# Function to suggest available slots for a new class
def suggest_available_slots(new_class, new_class_slots):
    all_slots = set.union(*class_schedule.values())
    available_slots = all_slots.difference(new_class_slots)
    print(f"Available slots for {new_class}: {available_slots}")

# Detect conflicts
detect_conflicts("Math", "Physics")
detect_conflicts("History", "Chemistry")

# Suggest available slots for a new class
suggest_available_slots("Biology", {"09:00-10:30", "15:00-16:30"})
