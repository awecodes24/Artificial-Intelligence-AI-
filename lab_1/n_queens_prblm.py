# The problem is to place 8 queens on a chessboard so that no two queens are in the
# same row, column or diagonal.

import pprint

def isSafe(board, x, y, n):
    # Checking whether the column is filled
    for row in range(x):
        if board[row][y] == 'Q':
            return False
        
    # Checking for top left diagonals are filled
    row = x
    col = y
    while row>=0 and col>=0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1
        
    # Checking for top right diagonals are filled
    row = x
    col = y
    while row>=0 and col<n:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col += 1
    # return True if all the aforementioned tests is passed 
    return True

