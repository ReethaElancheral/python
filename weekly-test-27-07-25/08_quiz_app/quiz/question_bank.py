import json
from .question import MCQQuestion, TrueFalseQuestion

def load_questions(filename):
    questions = []
    with open(filename, 'r') as f:
        data = json.load(f)
        for item in data:
            qtype = item.get("type", "mcq")
            difficulty = item.get("difficulty", "easy")
            prompt = item["prompt"]
            answer = item["answer"]
            if qtype == "mcq":
                options = item["options"]
                questions.append(MCQQuestion(prompt, options, answer, difficulty))
            elif qtype == "tf":
                questions.append(TrueFalseQuestion(prompt, answer, difficulty))
    return questions

def save_questions(filename, questions):
    data = []
    for q in questions:
        if isinstance(q, MCQQuestion):
            data.append({
                "type": "mcq",
                "prompt": q.prompt,
                "options": q.options,
                "answer": q.answer,
                "difficulty": q.difficulty
            })
        elif isinstance(q, TrueFalseQuestion):
            data.append({
                "type": "tf",
                "prompt": q.prompt,
                "answer": q.answer,
                "difficulty": q.difficulty
            })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
