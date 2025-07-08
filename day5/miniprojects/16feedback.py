# ✅ 16. Feedback Collector

# Objective: Accept feedbacks until user types “exit”.
# Requirements:
# Use while loop.
# Use continue if feedback is under 3 characters.
# Use break when “exit” is typed.

while True:
    feedback = input("Enter your feedback (type 'exit' to stop): ").strip()
    
    if feedback.lower() == "exit":
        print("Feedback collection stopped.")
        break
    
    if len(feedback) < 3:
        print("Feedback too short, please enter at least 3 characters.")
        continue
    
    print(f"Feedback recorded: {feedback}")
