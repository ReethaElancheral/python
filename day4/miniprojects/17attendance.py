# ✅ 17. Attendance Pattern with Pass


# Objective: Skip processing for Sunday using pass.
# Requirements:
# Days list.
# If day is “Sunday”, use pass (reserved for future logic).
# Else, print “Marked Present”.

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    if day == "Sunday":
        pass 
    else:
        print(f"{day}: Marked Present")
