import random
from .decorators import validate_move

class TicTacToe:
    def __init__(self):
        self.board = [[" "]*3 for _ in range(3)]
        self.current_player = "X"  # Player is 'X', computer is 'O'

    def display(self):
        print("\n  0   1   2")
        for i, row in enumerate(self.board):
            print(i, " | ".join(row))
            if i < 2:
                print("  " + "---+---+---")

    def empty_cells_generator(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    yield (r, c)

    @validate_move
    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        b = self.board
        lines = (
            # rows
            [b[0][0], b[0][1], b[0][2]],
            [b[1][0], b[1][1], b[1][2]],
            [b[2][0], b[2][1], b[2][2]],
            # columns
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            # diagonals
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        )
        for line in lines:
            if line[0] == line[1] == line[2] != " ":
                return True
        return False

    def check_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def ai_move(self):
        empty_cells = list(self.empty_cells_generator())
        if not empty_cells:
            return False
        row, col = random.choice(empty_cells)
        self.board[row][col] = self.current_player
        return True
