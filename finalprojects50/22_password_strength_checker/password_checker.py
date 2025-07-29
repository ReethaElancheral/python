import string

# Generator: Yield missing criteria
def password_criteria(password):
    if len(password) < 6:
        yield "Password should be at least 6 characters long"
    if not any(c.isupper() for c in password):
        yield "Add at least one uppercase letter"
    if not any(c.islower() for c in password):
        yield "Add at least one lowercase letter"
    if not any(c.isdigit() for c in password):
        yield "Add at least one number"
    if not any(c in string.punctuation for c in password):
        yield "Add at least one special character"

# Strength thresholds
thresholds = {
    "Weak": range(0, 3),
    "Medium": range(3, 5),
    "Strong": range(5, 6)
}

# Function to evaluate strength
def evaluate_strength(password):
    score = 0

    if len(password) >= 6:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    for strength, range_val in thresholds.items():
        if score in range_val:
            return strength, score

    return "Unknown", score
