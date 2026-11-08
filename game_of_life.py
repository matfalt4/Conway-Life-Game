def count_neighbors(board, row, col):

    rows,cols = board.shape()

    neighbors = 0

    for i in range(row-1, row+2):
        for j in range(col-1, col+2):

            if i == row and j == col:
                continue;

            if 0 <= i < row and 0 <= j < col:
                neighbors += board[i, j]

    return neighbors
