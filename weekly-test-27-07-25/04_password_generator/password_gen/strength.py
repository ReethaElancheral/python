import string

def password_strength(password):
    score = 0
    length = len(password)

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score >= 6:
        return "Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"
