class Question:
    def __init__(self, prompt, answer, difficulty="easy"):
        self.prompt = prompt
        self.answer = answer
        self.difficulty = difficulty

    def check_answer(self, response):
        return str(response).strip().lower() == str(self.answer).strip().lower()

class MCQQuestion(Question):
    def __init__(self, prompt, options, answer, difficulty="easy"):
        super().__init__(prompt, answer, difficulty)
        self.options = options

class TrueFalseQuestion(Question):
    def __init__(self, prompt, answer, difficulty="easy"):
        assert isinstance(answer, bool), "Answer must be boolean"
        super().__init__(prompt, answer, difficulty)
