import pygame
import numpy as np

def draw_grid(screen, board, CELL_SIZE):

    rows, cols = board.shape

    for row in range(rows):
        for col in range(cols):

            x = col*CELL_SIZE
            y = row*CELL_SIZE

            if board[row, col] == 1:
                
                pygame.draw.rect(
                    screen,
                    (0, 200, 100),
                    (x,y,CELL_SIZE,CELL_SIZE)
                )

            pygame.draw.rect(screen, (80, 80, 80), (x,y,CELL_SIZE,CELL_SIZE), 1)
