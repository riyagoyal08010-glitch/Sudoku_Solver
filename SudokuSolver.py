# Importing pprint to print the Sudoku board neatly
from pprint import pprint


# -----------------------------------------------
# Function 1: Find the next empty cell in the puzzle
# -----------------------------------------------
def find_next_empty(puzzle):
    """
    Finds the next empty spot (-1) in the puzzle.
    Returns the position as (row, col).
    If no empty spot is found, returns (None, None).
    """
    for r in range(9):               # Loop over each row (0–8)
        for c in range(9):           # Loop over each column (0–8)
            if puzzle[r][c] == -1:   # Check if the current cell is empty
                return r, c           # Return its position immediately
    return None, None                 # If no empty cell, puzzle is complete


# -----------------------------------------------
# Function 2: Check if a guess is valid
# -----------------------------------------------
def is_valid(puzzle, guess, row, col):
    """
    Checks whether placing 'guess' at (row, col) follows Sudoku rules:
      1. Number not already in the row
      2. Number not already in the column
      3. Number not already in its 3x3 box
    """

    # ---- Rule 1: Check the row ----
    row_vals = puzzle[row]             # Get the entire row
    if guess in row_vals:              # If guess already present in row
        return False                   # Not valid

    # ---- Rule 2: Check the column ----
    col_vals = [puzzle[i][col] for i in range(9)]  # Get all values in that column
    if guess in col_vals:              # If guess already present in column
        return False                   # Not valid

    # ---- Rule 3: Check the 3x3 sub-grid ----
    # Find the top-left corner of the 3x3 box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # Loop through the 3x3 box
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:  # If guess found in this 3x3 block
                return False            # Not valid

    # If all checks are passed, the guess is valid
    return True


# -----------------------------------------------
# Function 3: Solve the Sudoku using Backtracking
# -----------------------------------------------
def solve_sudoku(puzzle):
    """
    Solves the Sudoku puzzle using a backtracking algorithm.
    Modifies the 'puzzle' in place.
    Returns True if solved successfully, False otherwise.
    """

    # Step 1: Choose a place on the board to make a guess
    row, col = find_next_empty(puzzle)

    # Step 2: If no empty places are left, puzzle is solved!
    if row is None:
        return True

    # Step 3: Try all possible numbers (1–9)
    for guess in range(1, 10):
        # Step 4: Check if the number is valid
        if is_valid(puzzle, guess, row, col):
            # Step 5: Place the guess temporarily
            puzzle[row][col] = guess

            # Step 6: Recursively solve the rest of the puzzle
            if solve_sudoku(puzzle):
                return True  # If successful, return True

        # Step 7: If not valid or puzzle unsolved later, backtrack
        puzzle[row][col] = -1  # Reset to empty and try next number

    # Step 8: If no number works, return False (backtrack to previous call)
    return False


# -----------------------------------------------
# Main Program: Define the Sudoku board and solve it
# -----------------------------------------------
if __name__ == '__main__':   #run this block only when file being run directly not imported
    # -1 represents empty cells
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]

    print("Original Sudoku Board:")
    pprint(example_board)              # Print the unsolved Sudoku

    print("\nSolving...\n")
    solve_sudoku(example_board)        # Call the solver

    print("Solved Sudoku Board:")
    pprint(example_board)              # Print the solved Sudoku
