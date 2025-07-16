# 14. Election Vote Counter

# Description: Count votes by candidate.
# Requirements:
# - {candidate_name: vote_count}
# - Increment votes using .get(name, 0)+1
# - Show winner
# - Detect invalid votes (not in candidate list)

candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

def cast_vote(candidate_name):
    """Cast a vote for a candidate."""
    if candidate_name in candidates:
        candidates[candidate_name] += 1
    else:
        print(f"Invalid vote: {candidate_name} is not a valid candidate.")

def get_winner():
    """Determine the winner based on the highest vote count."""
    if not candidates:
        return None
    winner = max(candidates, key=candidates.get)
    return winner


cast_vote("Alice")
cast_vote("Bob")
cast_vote("Alice")
cast_vote("David")  

winner = get_winner()
if winner:
    print(f"The winner is {winner} with {candidates[winner]} votes.")
else:
    print("No valid votes cast.")

 