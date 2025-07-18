from poll.poll_utils import cast_vote, display_results

def main():
    voter_set = set()
    poll_results = {}

    print("Welcome to the Online Polling System")

    while True:
        print("\n1. Cast Vote")
        print("2. View Results")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            voter_id = input("Enter Voter ID: ").strip()
            candidate = input("Enter candidate name: ").strip().title()
            cast_vote(voter_id, candidate, voter_set, poll_results)

        elif choice == '2':
            display_results(poll_results)

        elif choice == '3':
            print("Thanks for participating!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
