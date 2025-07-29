import json

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        return self.answer.lower() == user_answer.lower()

class QuizGame:
    def __init__(self, file_path="quiz/questions.json"):
        self.file_path = file_path
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Question(**q) for q in data]
        except FileNotFoundError:
            print("❌ Questions file not found.")
            return []
        except Exception as e:
            print("⚠️ Error loading questions:", e)
            return []

    def question_generator(self):
        for question in self.questions:
            yield question

    def start_quiz(self):
        print("\n🎯 Starting Quiz...\n")
        for q in self.question_generator():
            print(q.question)
            for idx, opt in enumerate(q.options, 1):
                print(f"{idx}. {opt}")
            try:
                user_choice = int(input("Your answer (1-4): "))
                if 1 <= user_choice <= 4:
                    selected_option = q.options[user_choice - 1]
                    if q.is_correct(selected_option):
                        print("✅ Correct!\n")
                        self.score += 1
                    else:
                        print(f"❌ Wrong! Correct answer is: {q.answer}\n")
                else:
                    print("⚠️ Invalid option. Skipping question.\n")
            except ValueError:
                print("⚠️ Invalid input. Must be a number.\n")

    def calculate_score(self):
        total = len(self.questions)
        print(f"📊 Your Score: {self.score}/{total}")
        percentage = (self.score / total) * 100 if total else 0
        print(f"🎉 Result: {round(percentage, 2)}%")
