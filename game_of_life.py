import numpy as np


def count_neighbors(board:np.ndarray, row:int, col:int)->int:

    rows,cols = board.shape

    neighbors = 0

    for i in range(row-1, row+2):
        for j in range(col-1, col+2):

            if i == row and j == col:
                continue

            neighbors += board[i%rows, j%cols]

    return neighbors

###############################################################################################

def new_generation(board:np.ndarray)->np.ndarray:

    rows,cols = board.shape

    new_board = board.copy()

    for row in range(rows):
        for col in range(cols):

            neighbors = count_neighbors(board, row,col)

            if board[row,col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[row,col] = 0

            elif board[row, col] == 0:
                if neighbors == 3:
                    new_board[row,col] = 1

    return new_board     

###############################################################################################
