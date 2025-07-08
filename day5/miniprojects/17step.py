# ✅ 17. Step Tracker

# Objective: Track steps walked daily.
# Requirements:
# Input steps daily for 7 days.
# If any entry is 0, skip with continue.
# After 7 entries, print total and average using else.

total_steps = 0
day = 1

while day <= 7:
    steps = int(input(f"Enter steps walked on day {day}: "))
    
    if steps == 0:
        print("No steps recorded for this day, skipping.")
        continue  
    
    total_steps += steps
    day += 1

else:
    average_steps = total_steps / 7
    print(f"Total steps walked in 7 days: {total_steps}")
    print(f"Average steps per day: {average_steps:.2f}")
