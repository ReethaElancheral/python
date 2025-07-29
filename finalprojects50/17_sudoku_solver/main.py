# 17. Sudoku Solver 
# Objective: Solve a 9x9 Sudoku grid. 
# Requirements: 
#  OOP: Sudoku class (grid). 
#  List of Lists: Represent the Sudoku board. 
#  File Handling: Load puzzles from CSV. 
#  Exception Handling: Invalid grid input. 
#  Functions: Solve using backtracking. 
#  Conditionals: Check valid moves. 
#  Loops: Iterate through cells. 
#  Generator: Yield possible numbers for a cell. 
#  Decorator: @timeit to measure solving time. 

from sudoku.core import Sudoku

def main():
   
    puzzle = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
    ]

    sudoku = Sudoku(puzzle)
    print("Original Puzzle:")
    sudoku.display()

    if sudoku.solve():
        print("\nSolved Puzzle:")
        sudoku.display()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
