def validate_move(func):
    def wrapper(self, row, col):
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("⚠️ Invalid move: position out of range (0-2).")
            return False
        if self.board[row][col] != " ":
            print("⚠️ Invalid move: cell already occupied.")
            return False
        return func(self, row, col)
    return wrapper
