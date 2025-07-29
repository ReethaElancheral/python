# 18. Tic-Tac-Toe Game 
# Objective: Play against the computer. 
# Requirements: 
#  OOP: TicTacToe class (board, current player). 
#  List of Lists: 3x3 grid. 
#  Exception Handling: Invalid moves. 
#  Functions: Check win/draw, AI move (random). 
#  Conditionals: Alternate turns. 
#  Loops: Game loop until win/draw. 
#  Generator: Yield empty cells. 
#  Decorator: @validate_move for position checks.



from tic_tac_toe.core import TicTacToe

def main():
    print("🎮 Tic-Tac-Toe Game (You are X, Computer is O)")

    game = TicTacToe()
    game.display()

    while True:
        if game.current_player == "X":
            # Player's turn
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("⚠️ Please enter valid integers 0-2.")
                continue

            if not game.make_move(row, col):
                continue

        else:
            # Computer's turn
            print("🤖 Computer is making a move...")
            game.ai_move()

        game.display()

        if game.check_win():
            winner = "You" if game.current_player == "X" else "Computer"
            print(f"🏆 {winner} won!")
            break
        if game.check_draw():
            print("🤝 It's a draw!")
            break

        game.switch_player()

if __name__ == "__main__":
    main()
