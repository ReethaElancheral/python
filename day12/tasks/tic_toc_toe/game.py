from .player import get_move
from .board import init_board, display

def play():
    board = init_board()
    player = "X"
    for _ in range(9):
        display(board)
        move = get_move(player)
        board[move] = player
        player = "O" if player == "X" else "X"
    display(board)
    print("Game over!")

if __name__ == "__main__":
    play()
