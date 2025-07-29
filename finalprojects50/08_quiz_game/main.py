from quiz.core import QuizGame
from quiz.utils import timer

@timer
def run_quiz():
    game = QuizGame()
    if not game.questions:
        print("No questions to run the quiz.")
        return
    game.start_quiz()
    game.calculate_score()

if __name__ == "__main__":
    print("🧠 Welcome to the CLI Quiz Game!")
    run_quiz()
