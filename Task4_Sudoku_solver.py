def print_grid(grid):
    """Print the Sudoku grid in a formatted way."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty_location(grid):
    """Find an empty location in the grid (denoted by 0)."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_safe(grid, row, col, num):
    """Check if it's safe to place a number in a specific location."""
    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
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
                return True  # Solution found

            grid[row][col] = 0  # Reset if no solution found

    return False  # Trigger backtracking

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
