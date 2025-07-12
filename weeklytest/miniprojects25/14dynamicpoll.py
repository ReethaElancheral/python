# 14. Dynamic Polling App

# Concepts: list, functions, strings, while.
# Ask user a poll question.
# Record options and votes.
# Show results dynamically.
# Allow multiple users.

def create_poll():
    question = input("Enter the poll question: ").strip()
    options = []
    print("Enter poll options one by one (type 'done' when finished):")
    while True:
        option = input(f"Option {len(options)+1}: ").strip()
        if option.lower() == 'done':
            if len(options) < 2:
                print("Please enter at least two options.")
                continue
            break
        elif option == '':
            print("Option cannot be empty.")
        else:
            options.append(option)
    votes = [0] * len(options)
    return question, options, votes

def display_poll(question, options, votes):
    print(f"\nPoll Question: {question}")
    for i, (opt, count) in enumerate(zip(options, votes), start=1):
        print(f"{i}. {opt} - Votes: {count}")
    print()

def vote_poll(options, votes):
    while True:
        choice = input(f"Enter your vote (1-{len(options)}): ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                votes[choice - 1] += 1
                print(f"Vote counted for '{options[choice - 1]}'")
                break
            else:
                print("Invalid choice number.")
        else:
            print("Please enter a number.")

def polling_app():
    question, options, votes = create_poll()

    while True:
        display_poll(question, options, votes)
        vote_poll(options, votes)
        cont = input("Another user wants to vote? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("\nFinal Poll Results:")
            display_poll(question, options, votes)
            print("Thank you for participating!")
            break

polling_app()
