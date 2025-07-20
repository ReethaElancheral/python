def tally_votes(votes):
    print("\nCurrent Vote Tally:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

def announce_winner(votes):
    if not votes:
        print("No votes recorded.")
        return

    max_votes = max(votes.values())
    winners = [candidate for candidate, count in votes.items() if count == max_votes]

    print("\n=== Election Result ===")
    if len(winners) == 1:
        print(f"Winner: {winners[0]} with {max_votes} votes!")
    else:
        print("It's a tie between:")
        for w in winners:
            print(f"- {w} ({votes[w]} votes)")
