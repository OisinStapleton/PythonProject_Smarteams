import random

def generateAlgorithm(grid, x, y):
    flagMatch = False
    for h in range(-3,9):
        if (h <= 0):
            h = random.randint(1, 9)
        grid[x][y] = h
        flagMatch = False
        for i in range(9):
            if grid[x][y] == grid[i][y]:
                if(i == x):
                    continue
                flagMatch = True
            for j in range(9):
                if(j == y):
                    continue
                if grid[x][y] == grid[x][j]:
                    flagMatch = True
        if not flagMatch:
            return h
    return 0

def generateGrid():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for y in range(9):
        for x in range(9):
            grid[x][y] = generateAlgorithm(grid,x,y)
            if grid[x][y] == 0:
                x -= 2
                if x == 8:
                    y -= 2
    return grid

def printGrid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))


grid = generateGrid()
printGrid(grid)
