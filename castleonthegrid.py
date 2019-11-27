
import sys
from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    
    n = len(grid)
    start = (startX, startY)

    distances = {(x, y): sys.maxsize for x in range(n) for y in range(n)}
    distances[start] = 0

    stack = deque()
    stack.append(start)

    while stack:
        
        nextX, nextY = stack.pop()
        d = distances[(nextX, nextY)]

        if (nextX, nextY) == (goalX, goalY):
            return d

        nexts = []

        #up
        x = nextX - 1
        while x > -1 and grid[x][nextY] != 'X':
            nexts.append((x, nextY))
            x -= 1

        #down
        x = nextX + 1
        while x < n and grid[x][nextY] != 'X':
            nexts.append((x, nextY))
            x += 1

        #left
        y = nextY - 1
        while y > -1 and grid[nextX][y] != 'X':
            nexts.append((nextX, y))
            y -= 1

        # right
        y = nextY + 1
        while y < n and grid[nextX][y] != 'X':
            nexts.append((nextX, y))
            y += 1
    
        for cells in nexts:
            if d + 1 < distances[cells]:
                distances[cells] = d + 1
                stack.appendleft(cells)

if __name__ == '__main__':

    grid = [['.', '.', '.'],['.', 'X', '.'],['.', '.', '.']]
    startXStartY = [0, 0, 1, 2]

    # grid = [['.', 'X', '.'],['.', 'X', '.'],['.', '.', '.']]
    # startXStartY = [0, 0, 0, 2]

    # grid = [['.', '.', '.'],['.', 'X', '.'],['.', 'X', '.']]
    # startXStartY = [2, 0, 0, 2]

    # grid = [['.', '.', '.'],['.', 'X', '.'],['.', 'X', '.']]
    # startXStartY = [2, 0, 2, 2]
    # grid = [
    # ['.','X','.','.','X','X','.','.','.','X'],
    # ['X','.','.','.','.','.','.','.','.','.'],
    # ['.','X','.','.','.','.','.','.','.','X'],
    # ['.','.','.','.','.','.','.','.','.','.'],
    # ['.','.','.','.','.','.','.','.','X','.'],
    # ['.','X','.','.','.','X','X','X','.','.'],
    # ['.','.','.','.','.','X','.','.','X','X'],
    # ['.','.','.','.','.','X','.','X','.','.'],
    # ['.','.','.','.','.','.','.','.','.','.'],
    # ['.','.','.','.','.','X','.','.','X','X']]
    # startXStartY = [9, 1, 9, 6]

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(str(result) + '\n')
