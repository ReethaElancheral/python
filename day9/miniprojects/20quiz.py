# 20. Quiz Score Analyzer

# Goal: Record quiz attempts and analyze scores.
# Requirements:
# Store data as (user_id, (quiz1, quiz2, quiz3))
# Calculate best and worst scores.
# Tuple slicing to get last 2 attempts.
# Replace tuple after final submission.


quiz_attempts = []


def add_quiz_attempt(user_id, scores):
    quiz_attempts.append((user_id, scores))


def calculate_best_worst_scores():
    user_scores = {}
    for user_id, (quiz1, quiz2, quiz3) in quiz_attempts:
        total_score = quiz1 + quiz2 + quiz3
        if user_id not in user_scores:
            user_scores[user_id] = {'best': total_score, 'worst': total_score}
        else:
            user_scores[user_id]['best'] = max(user_scores[user_id]['best'], total_score)
            user_scores[user_id]['worst'] = min(user_scores[user_id]['worst'], total_score)
    return user_scores


def display_best_worst_scores():
    user_scores = calculate_best_worst_scores()
    print("\n🏆 Best and Worst Scores by User")
    print("----------------------------------")
    for user_id, scores in user_scores.items():
        print(f"User {user_id}: Best Score = {scores['best']}, Worst Score = {scores['worst']}")
    print("----------------------------------")


def get_recent_attempts(n):
    print(f"\n📝 Last {n} Quiz Attempts")
    print("---------------------------")
    for user_id, (quiz1, quiz2, quiz3) in quiz_attempts[-n:]:
        print(f"User {user_id}: Quiz1 = {quiz1}, Quiz2 = {quiz2}, Quiz3 = {quiz3}")
    print("---------------------------")


add_quiz_attempt("user1", (8, 7, 9))
add_quiz_attempt("user2", (6, 8, 7))
add_quiz_attempt("user1", (9, 9, 10))
add_quiz_attempt("user3", (7, 6, 8))


display_best_worst_scores()


get_recent_attempts(2)
