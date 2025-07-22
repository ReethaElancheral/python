import csv
from datetime import datetime
import os

RESULTS_FILE = "results.csv"

def load_questions(filename):
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("❌ Questions file not found.")
        return []

def take_quiz(questions):
    print("\nStart the quiz!\n")
    score = 0
    for i, q in enumerate(questions, start=1):
        answer = input(f"Q{i}: {q['question']} ").strip()
        if answer.lower() == q['answer'].lower():
            print("✔️ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! Correct answer: {q['answer']}")
    print(f"\nYour score: {score} out of {len(questions)}")
    return score

def save_result(name, score, total):
    file_exists = os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Score", "Total", "Date"])
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([name, score, total, date_str])
