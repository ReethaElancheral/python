# 24. Feedback Collector with Sentiment Count

# Concepts: strings, list, functions.
# Collect feedback.
# Count how many are "good", "bad", "average".
# Use in, lower(), etc.



def collect_feedback():
    feedbacks = []
    sentiments = {"good": 0, "bad": 0, "average": 0}

    while True:
        fb = input("Enter feedback (or type 'done' to finish): ").strip()
        if fb.lower() == 'done':
            break
        feedbacks.append(fb)

        fb_lower = fb.lower()
        if "good" in fb_lower:
            sentiments["good"] += 1
        elif "bad" in fb_lower:
            sentiments["bad"] += 1
        elif "average" in fb_lower:
            sentiments["average"] += 1

    return feedbacks, sentiments

def show_summary(feedbacks, sentiments):
    print("\n--- Feedback Summary ---")
    print(f"Total feedbacks: {len(feedbacks)}")
    print(f"Good: {sentiments['good']}")
    print(f"Bad: {sentiments['bad']}")
    print(f"Average: {sentiments['average']}")

feedbacks, sentiments = collect_feedback()
show_summary(feedbacks, sentiments)
