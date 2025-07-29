import csv
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

class Sudoku:
    def __init__(self, grid=None):
        if grid:
            if not self._validate_grid(grid):
                raise ValueError("Invalid Sudoku grid.")
            self.grid = grid
        else:
            # Initialize empty 9x9 grid
            self.grid = [[0]*9 for _ in range(9)]

    def _validate_grid(self, grid):
        # Check grid size and values 0-9
        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            return False
        for row in grid:
            for val in row:
                if not (0 <= val <= 9):
                    return False
        return True

    @staticmethod
    def load_puzzles(filename="sudoku/puzzles.csv"):
        puzzles = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Expecting 81 comma-separated values per row (one puzzle)
                if len(row) != 81:
                    continue
                puzzle = [list(map(int, row[i*9:(i+1)*9])) for i in range(9)]
                puzzles.append(puzzle)
        return puzzles

    @timeit
    def solve(self):
        empty = self._find_empty()
        if not empty:
            return True  # Solved
        row, col = empty
        for num in self._possible_numbers(row, col):
            self.grid[row][col] = num
            if self.solve():
                return True
            self.grid[row][col] = 0  # backtrack
        return False

    def _find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return r, c
        return None

    def _possible_numbers(self, row, col):
        """Generator yielding valid numbers for grid[row][col]."""
        used = set()

        # Check row
        used.update(self.grid[row])

        # Check column
        used.update(self.grid[r][col] for r in range(9))

        # Check 3x3 box
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                used.add(self.grid[r][c])

        for num in range(1, 10):
            if num not in used:
                yield num

    def display(self):
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-"*21)
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(val if val != 0 else ".", end=" ")
            print()
