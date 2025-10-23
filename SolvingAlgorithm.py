def algorithm(grid, x, y):
    flagMatch = False
    for h in range(9):
        grid[x][y] = h
        flagMatch = False
        for i in range(9):
            if grid[x][y] == grid[i][y]:
                flagMatch = True
            for j in range(9):
                if grid[x][y] == grid[x][j]:
                    flagMatch = True
        if not flagMatch:
            return h
    return -1


def solve(grid):
    for y in range(9):
        for x in range(9):
            grid[x][y] = algorithm(x, y)
            if grid[x][y] == -1:
                x -= 1
                if x == -1:
                    y -= 1
                    x = 8


