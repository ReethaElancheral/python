from voting_system.voting import vote
from voting_system.tally import tally_votes, announce_winner

def main():
    candidates = {"Alice", "Bob", "Charlie"}
    voters = set()
    votes = {candidate: 0 for candidate in candidates}

    while True:
        print("\n==== Voting Menu ====")
        print("1. Vote")
        print("2. Tally Votes")
        print("3. Announce Winner")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter your voter name: ").strip()
            print(f"Candidates: {', '.join(candidates)}")
            selected = input("Enter candidate name: ").strip()
            vote(name, selected, candidates, voters, votes)

        elif choice == '2':
            tally_votes(votes)

        elif choice == '3':
            announce_winner(votes)

        elif choice == '4':
            print("Exiting Voting System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
