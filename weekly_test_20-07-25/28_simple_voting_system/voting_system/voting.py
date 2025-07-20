def vote(voter_name, candidate, candidates, voters, votes):
    if voter_name in voters:
        print("You have already voted.")
        return

    if candidate not in candidates:
        print("Invalid candidate name.")
        return

    votes[candidate] += 1
    voters.add(voter_name)
    print(f"Vote recorded for {candidate}. Thank you, {voter_name}!")
