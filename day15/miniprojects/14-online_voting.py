# 14. Online Voting System

# Use Case: Allow users to vote once per session. 
# Exception Handling Goals:
# Raise AlreadyVotedError if user tries again
# Catch unexpected errors and log
# Use finally to display thanks message

import logging

# Setup logging
logging.basicConfig(filename="voting_errors.log", level=logging.ERROR)

# Custom Exception
class AlreadyVotedError(Exception):
    pass

class VotingSystem:
    def __init__(self):
        self.voted_users = set()

    def vote(self, user_id):
        try:
            if user_id in self.voted_users:
                raise AlreadyVotedError("User has already voted.")
            # Simulate voting process
            self.voted_users.add(user_id)
            print(f"✅ Vote recorded for user: {user_id}")
        except AlreadyVotedError as ave:
            logging.error(f"{user_id}: {ave}")
            print(f"❌ {ave}")
        except Exception as e:
            logging.error(f"Unexpected error for user {user_id}: {e}", exc_info=True)
            print(f"❌ Unexpected error occurred: {e}")
        finally:
            print("🙏 Thank you for participating in the vote!")

if __name__ == "__main__":
    voting_system = VotingSystem()

    while True:
        user = input("\nEnter user ID to vote (or 'exit' to quit): ").strip()
        if user.lower() == 'exit':
            break
        voting_system.vote(user)
