# quiz/admin/questions.py
import json
import random
from pathlib import Path

def load_questions(num=5):
    """Load questions from JSON and pick `num` random ones."""
    path = Path(__file__).parent.parent / 'data' / 'questions.json'
    qlist = json.loads(path.read_text())
    return random.sample(qlist, min(num, len(qlist)))

if __name__ == "__main__":
    print(load_questions(3))
