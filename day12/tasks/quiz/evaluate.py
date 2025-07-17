def evaluate(questions, answers):
    return sum(1 for q,a in zip(questions, answers) if q[1].lower() == a.lower())
