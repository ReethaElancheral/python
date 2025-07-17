def init_board():
    return [" "] * 9

def display(board):
    print("\n".join([
        f"{board[0]}|{board[1]}|{board[2]}",
        "-+-+-",
        f"{board[3]}|{board[4]}|{board[5]}",
        "-+-+-",
        f"{board[6]}|{board[7]}|{board[8]}"
    ]))
