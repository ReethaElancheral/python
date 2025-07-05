# ✅ 16. Weekly Task Tracker

# Objective: Display daily tasks using enumerate().
# Requirements:
# Predefined task list.
# Use loop with enumerate() starting from Monday.
# Output:
# arduinoCopyEditMonday: Task 1  
# Tuesday: Task 2  
# ...


tasks = [
    "Prepare report",
    "Team meeting",
    "Code review",
    "Client call",
    "Update documentation",
    "Deploy changes",
    "Weekly summary"
]


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for index, task in enumerate(tasks):
    print(f"{days[index]}: {task}")
