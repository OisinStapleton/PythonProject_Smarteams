import random

def isValid(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False
    # Check column
    if num in [grid[r][col] for r in range(9)]:
        return False
    # Check 3x3 box
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if grid[r][c] == num:
                return False
    return True

def solveSudoku(grid, row=0, col=0):
    if row == 9:
        return True  # Completed
    if col == 9:
        return solveSudoku(grid, row + 1, 0)  # Next row
    if grid[row][col] != 0:  # Skip pre-filled cell
        return solveSudoku(grid, row, col + 1)

    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if isValid(grid, row, col, num):
            grid[row][col] = num
            if solveSudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0  # Backtrack
    return False

def generateSudoku():
    # Step 1: Generate a full Sudoku grid
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solveSudoku(grid)

    # Step 2: Randomly choose cells to remove (make negative)
    # Adjust the number (e.g., 40) to control difficulty
    cells_to_remove = random.sample(range(81), 40)
    for index in cells_to_remove:
        r, c = divmod(index, 9)
        grid[r][c] = -grid[r][c]  # Mark as question

    return grid

def printGrid(grid):
    for row in grid:
        print("".join(f"{num:3d}" for num in row))

# Example usage
sudoku = generateSudoku()
printGrid(sudoku)