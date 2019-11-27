
import sys
from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    
    length = len(grid)
    start = (startX, startY)

    distances = {(x, y): sys.maxsize for x in range(length) for y in range(length)}
    distances[start] = 0

    q = deque()
    q.append(start)

    while q:
        
        currX, currY = q.pop()
        d = distances[(currX, currY)]

        if (currX, currY) == (goalX, goalY):
            return d

        adjacents = []

        #up
        nextX = currX - 1
        while nextX > -1 and not blocked(grid, nextX, currY):
            adjacents.append((nextX, currY))
            nextX -= 1
        #down
        nextX = currX + 1
        while nextX < length and not blocked(grid, nextX, currY):
            adjacents.append((nextX, currY))
            nextX += 1
        #left
        nextY = currY - 1
        while nextY > -1 and not blocked(grid, currX, nextY):
            adjacents.append((currX, nextY))
            nextY -= 1
        # right
        nextY = currY + 1
        while nextY < length and not blocked(grid, currX, nextY):
            adjacents.append((currX, nextY))
            nextY += 1
    
        for cells in adjacents:
            if d + 1 < distances[cells]:
                distances[cells] = d + 1
                q.appendleft(cells)

def blocked(grid, x, y):
    return grid[x][y] == 'X'



if __name__ == '__main__':

    grid = [['.', '.', '.'],['.', 'X', '.'],['.', '.', '.']]
    startXStartY = [0, 0, 1, 2]

    # grid = [['.', 'X', '.'],['.', 'X', '.'],['.', '.', '.']]
    # startXStartY = [0, 0, 0, 2]

    grid = [['.', '.', '.'],['.', 'X', '.'],['.', 'X', '.']]
    startXStartY = [2, 0, 0, 2]

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
