def show_stats(stats):
    total = stats["correct"] + stats["incorrect"]
    print("\n--- Stats ---")
    print(f"Correct: {stats['correct']}")
    print(f"Incorrect: {stats['incorrect']}")
    print(f"Total Attempts: {total}")
    if total:
        accuracy = (stats["correct"] / total) * 100
        print(f"Accuracy: {accuracy:.2f}%")
    else:
        print("No quiz attempts yet.")
