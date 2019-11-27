#!/bin/python3

import math
import os
import random
import re
import sys
import queue

class Cell: 
    row = 0
    col = 0
    def __init__(self, row, col): 
        self.row = row 
        self.col = col

    def __str__(self):
     return 'row: '+str(self.row)+' col:'+str(self.col)

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    start = Cell(startX, startY)
    visited = [[False for x in range(n)] for y in range(n)]

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 'X':
                visited[x][y] = True 
            else:
                visited[x][y] = False
  
    visited[start.row][start.col] = True 

    q = queue.Queue()
    q.put(start)
    
    turns = set()

    while not q.empty():
        
        cell = q.get()

        if goalX == cell.row and goalY == cell.col:
            break
        
        # Right
        if cell.col + 1 < n and not visited[cell.row][cell.col + 1]:
            right = Cell(cell.row, cell.col + 1)
            q.put(right) 
            print('Right '+str(right))
            visited[cell.row][cell.col + 1] = True
            turns.add('Right')
            continue

        # Down
        if cell.row + 1 < n and not visited[cell.row + 1][cell.col]:
            down = Cell(cell.row + 1, cell.col)
            q.put(down)
            print('Down  '+str(down))
            visited[cell.row + 1][cell.col] = True    
            turns.add('Down')
            continue
    
        # up
        if cell.row - 1 >= 0 and not visited[cell.row - 1][cell.col]:
            up = Cell(cell.row - 1, cell.col)
            q.put(up)
            print('Up    '+str(up))
            visited[cell.row - 1][cell.col] = True
            turns.add('Up')
            continue

        # Left
        if cell.col - 1 >= 0 and not visited[cell.row][cell.col - 1]:
            left = Cell(cell.row, cell.col - 1)
            q.put(left) 
            print('Left  '+str(left))
            visited[cell.row][Cell.col - 1] = True
            turns.add('Left')
            continue

    return len(turns)

if __name__ == '__main__':

    # grid = [['.', '.', '.'],['.', 'X', '.'],['.', '.', '.']]
    # startXStartY = [0, 0, 1, 2]

    # grid = [['.', 'X', '.'],['.', 'X', '.'],['.', '.', '.']]
    # startXStartY = [0, 0, 0, 2]

    # grid = [['.', '.', '.'],['.', 'X', '.'],['.', 'X', '.']]
    # startXStartY = [2, 0, 0, 2]

    # grid = [['.', '.', '.'],['.', 'X', '.'],['.', 'X', '.']]
    # startXStartY = [2, 0, 2, 2]
    grid = [
    ['.','X','.','.','X','X','.','.','.','X'],
    ['X','.','.','.','.','.','.','.','.','.'],
    ['.','X','.','.','.','.','.','.','.','X'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','X','.'],
    ['.','X','.','.','.','X','X','X','.','.'],
    ['.','.','.','.','.','X','.','.','X','X'],
    ['.','.','.','.','.','X','.','X','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','X','.','.','X','X']]
    startXStartY = [9, 1, 9, 6]

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(str(result) + '\n')
