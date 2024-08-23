def print_grid(grid):
    """Function to print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty_location(grid):
    """Find an empty location in the Sudoku grid."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None

def is_safe(grid, row, col, num):
    """Check if it's safe to place a number in a given position."""
    # Check the row
    if num in grid[row]:
        return False
    
    # Check the column
    if num in (grid[i][col] for i in range(len(grid))):
        return False
    
    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  # Puzzle solved
    row, col = empty_location
    
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0  # Backtrack

    return False

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_grid):
    print("Sudoku puzzle solved successfully!")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
