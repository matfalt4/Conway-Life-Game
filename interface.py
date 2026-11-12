import pygame
import numpy as np

def draw_grid(screen:pygame.Surface, board:np.ndarray, CELL_SIZE:int)->None:

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

###############################################################################################

def draw_panel(screen:pygame.Surface, rows:int, cell_size:int, panel_heiht:int, generation:int, font:pygame.font)->None:

    y = rows*cell_size

    pygame.draw.rect(screen,
                     (45,45,45),
                     (0,y,screen.get_width(),panel_heiht)
    )
