import pygame
import random
import sys

# --- Sudoku Logic ---
def isValid(grid, row, col, num):
    if num in grid[row]:
        return False
    if num in [grid[r][col] for r in range(9)]:
        return False
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if grid[r][c] == num:
                return False
    return True

def solveSudoku(grid, row=0, col=0):
    if row == 9:
        return True
    if col == 9:
        return solveSudoku(grid, row + 1, 0)
    if grid[row][col] != 0:
        return solveSudoku(grid, row, col + 1)

    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if isValid(grid, row, col, num):
            grid[row][col] = num
            if solveSudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False


def generateSudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solveSudoku(grid)
    cells_to_remove = random.sample(range(81), 40)
    for index in cells_to_remove:
        r, c = divmod(index, 9)
        grid[r][c] = -grid[r][c]
    return grid

# --- Pygame Setup ---
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

answerGrid = generateSudoku()
inputGrid = [row.copy() for row in answerGrid]
for i in range(9):
    for j in range(9):
        if inputGrid[i][j] > 0:
            inputGrid[i][j] = 0

selected = None

def draw_grid():
    screen.fill((255, 255, 255))
    # Draw cells
    for i in range(9):
        for j in range(9):
            value = abs(grid[i][j])
            if value != 0:
                color = (0, 0, 0) if grid[i][j] > 0 else (0, 0, 255)
                text = font.render(str(value), True, color)
                screen.blit(text, (j*60 + 20, i*60 + 10))
    # Draw grid lines
    for i in range(10):
        thick = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, (0, 0, 0), (0, i*60), (540, i*60), thick)
        pygame.draw.line(screen, (0, 0, 0), (i*60, 0), (i*60, 540), thick)
    # Highlight selected cell
    if selected:
        pygame.draw.rect(screen, (255, 0, 0), (selected[1]*60, selected[0]*60, 60, 60), 3)

def handle_input(key):
    global grid
    if selected and key in range(pygame.K_1, pygame.K_10):
        num = key - pygame.K_0
        row, col = selected
        if grid[row][col] < 0:  # Can only edit empty cells
            grid[row][col] = num

# --- Main Loop ---
running = True
while running:
    draw_grid()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            selected = (y // 60, x // 60)
        elif event.type == pygame.KEYDOWN:
            handle_input(event.key)

    clock.tick(60)

pygame.quit()
sys.exit()