from .timer import QuizTimer

class QuizManager:
    def __init__(self, questions, time_per_question=15):
        self.questions = questions
        self.score = 0
        self.time_per_question = time_per_question

    def run_quiz(self, difficulty=None):
        filtered_questions = [q for q in self.questions if difficulty is None or q.difficulty == difficulty]
        print(f"\nStarting quiz with {len(filtered_questions)} questions (Difficulty: {difficulty or 'all'})")

        for q in filtered_questions:
            print("\n" + q.prompt)
            if hasattr(q, 'options'):
                for i, opt in enumerate(q.options, 1):
                    print(f"  {i}. {opt}")

            timer = QuizTimer(self.time_per_question)
            timer.start()

            answer = input("Your answer: ")
            if timer.time_up:
                print("No answer recorded, moving to next question.")
                continue

            if hasattr(q, 'options'):
                try:
                    ans_idx = int(answer) - 1
                    if ans_idx < 0 or ans_idx >= len(q.options):
                        print("Invalid option number.")
                        continue
                    answer_val = q.options[ans_idx]
                except ValueError:
                    print("Please enter a valid number.")
                    continue
            else:
                answer_val = answer

            if q.check_answer(answer_val):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! Correct answer: {q.answer}")

        print(f"\nQuiz complete! Your score: {self.score} / {len(filtered_questions)}")
