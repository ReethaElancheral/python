import string

def add_feedback(feedback_db, customer_id, feedback_text):
    key = (customer_id,)
    if key in feedback_db:
        print(f"Customer {customer_id} already submitted feedback.")
        return

    feedback_db[key] = feedback_text.strip()
    print(f"Feedback received from Customer {customer_id}.")

def extract_keywords(feedback_text):
    
    translator = str.maketrans('', '', string.punctuation)
    cleaned = feedback_text.translate(translator).lower()
    words = cleaned.split()
    return set(words)

def display_feedback(feedback_db):
    if not feedback_db:
        print("No feedback available.")
        return

    print("\n--- All Customer Feedback ---")
    for customer, text in feedback_db.items():
        print(f"Customer ID: {customer[0]}")
        print(f"Feedback: {text}")
        keywords = extract_keywords(text)
        print(f"Keywords: {', '.join(sorted(keywords))}")
        print("-" * 40)
