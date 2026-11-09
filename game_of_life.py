def count_neighbors(board, row, col):

    rows,cols = board.shape

    neighbors = 0

    for i in range(row-1, row+2):
        for j in range(col-1, col+2):

            if i == row and j == col:
                continue;

            if 0 <= i < rows and 0 <= j < cols:
                neighbors += board[i, j]

    return neighbors

###############################################################################################

def new_generation(board):

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
