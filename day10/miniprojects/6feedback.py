# 6. Customer Feedback Analyzer

# Description: Categorize customer feedback into positive and negative.
# Requirements:
# - Structure: {customer_id: {"feedback": ..., "rating": ...}}
# - Use .values() to compute average rating
# - Count number of each feedback type using a summary dictionary
# - Use comprehension to extract customers with rating > 4


feedback_log = {
    101: {"feedback": "Great service", "rating": 5},
    102: {"feedback": "Okay experience", "rating": 3},
    103: {"feedback": "Terrible, very slow", "rating": 1},
    104: {"feedback": "Loved it", "rating": 4},
    105: {"feedback": "Not bad", "rating": 4}
}

def analyze_feedback(log):
  
    ratings = [info["rating"] for info in log.values()]
    avg = sum(ratings) / len(ratings) if ratings else 0

   
    summary = {"positive": 0, "neutral": 0, "negative": 0}
    for info in log.values():
        r = info["rating"]
        if r >= 4:
            summary["positive"] += 1
        elif r == 3:
            summary["neutral"] += 1
        else:
            summary["negative"] += 1

  
    high_raters = {cid: info for cid, info in log.items() if info["rating"] > 4}

    return avg, summary, high_raters


avg, summary, high_raters = analyze_feedback(feedback_log)


print(f"Average rating: {avg:.2f}")
print("Feedback summary:", summary)
print("High-rating customers:", high_raters)

