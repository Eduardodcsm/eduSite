# Function to check if placing 'number' at position (row, column) is valid
def is_valid_move(grid, row, column, number):
    # Check if 'number' is not in the same row
    for x in range(9):
        if grid[row][x] == number:
            return False
    
    # Check if 'number' is not in the same column
    for x in range(9):
        if grid[x][column] == number:
            return False
        
    # Check if 'number' is not in the same 3x3 square
    corner_row = row - row % 3
    corner_col = column - column % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    return True

# Function to solve the Sudoku puzzle using backtracking
def solve(grid, row, column):
    # If we reached the end of the grid, return True (puzzle solved)
    if column == 9:
        if row == 8:
            return True
        # Move to the next row and reset the column to 0
        row += 1
        column = 0

    # If the current cell is not empty, move to the next column
    if grid[row][column] > 0:
        return solve(grid, row, column + 1)

    # Try placing numbers 1 to 9 in the current cell
    for num in range(1, 10):
        # If placing 'num' is valid, update the grid and continue solving
        if is_valid_move(grid, row, column, num):
            grid[row][column] = num
            # Recursively try to solve the remaining puzzle
            if solve(grid, row, column + 1):
                return True
            # If the current placement doesn't lead to a solution, backtrack
            grid[row][column] = 0

    # No valid number was found, backtrack to the previous cell
    return False

# Initial Sudoku grid
grid = [
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

# Call the solve function to solve the Sudoku puzzle
if solve(grid, 0, 0):
    # If a solution exists, print the solved grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    # If no solution exists, print a message
    print("No solution exists.")
