def check_answer(user_answer, correct_answer):
    """
    Compare user answer to correct answer (case-insensitive, trimmed).
    Returns True if correct, False otherwise.
    """
    return user_answer.strip().lower() == correct_answer.strip().lower()
