# 10. Sports Team Roster

# Goal: Store player data in a sports team.
# Requirements:
# Store each player as: (player_id, name, (position, goals))
# Display players with more than 10 goals.
# Count how many strikers are in the team.
# Use tuple packing and unpacking to build team summary.


team_roster = [
    (1, "Alice", ("Forward", 15)),
    (2, "Bob", ("Midfielder", 8)),
    (3, "Charlie", ("Defender", 2)),
    (4, "David", ("Forward", 12)),
    (5, "Eve", ("Goalkeeper", 0)),
    (6, "Frank", ("Forward", 18)),
    (7, "Grace", ("Midfielder", 5)),
    (8, "Hannah", ("Defender", 1))
]


def display_top_scorers(roster):
    print("\n⚽ Players with More Than 10 Goals")
    print("----------------------------------")
    for player_id, name, (position, goals) in roster:
        if goals > 10:
            print(f"{name} ({position}) - Goals: {goals}")
    print("----------------------------------")


def count_strikers(roster):
    return sum(1 for _, _, (position, _) in roster if position == "Forward")


def team_summary(roster):
    total_goals = sum(goals for _, _, (_, goals) in roster)
    total_players = len(roster)
    avg_goals = total_goals / total_players if total_players > 0 else 0
    print("\n📊 Team Summary")
    print(f"Total Players: {total_players}")
    print(f"Total Goals: {total_goals}")
    print(f"Average Goals per Player: {avg_goals:.2f}")
    print(f"Number of Strikers: {count_strikers(roster)}")
    print("----------------------------------")


display_top_scorers(team_roster)


team_summary(team_roster)
