
def cast_vote(voter_id, candidate, voter_set, poll_results):
    voter_key = (voter_id,)

    if voter_key in voter_set:
        print(f"Voter {voter_id} has already voted!")
        return

    voter_set.add(voter_key)

    if candidate not in poll_results:
        poll_results[candidate] = 0

    poll_results[candidate] += 1
    print(f"Vote cast for {candidate} by Voter {voter_id}.")

def display_results(poll_results):
    print("\n--- Poll Results ---")
    if not poll_results:
        print("No votes yet.")
        return

    for candidate, count in poll_results.items():
        print(f"{candidate}: {count} votes")

    
    winner = max(poll_results, key=poll_results.get)
    print(f"\nWinner: {winner} with {poll_results[winner]} votes")
