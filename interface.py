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

def draw_panel(screen:pygame.Surface, rows:int, cell_size:int, panel_heiht:int, generation:int, font:pygame.font, sim_run:bool)->None:

    y = rows*cell_size

    pygame.draw.rect(
        screen,
        (45,45,45),
        (0,y,screen.get_width(),panel_heiht)
    )

    text = font.render(
        f"Generation: {generation}",
        True,
        (255,255,255)
    )

    if sim_run:
        status = "Running...:
    else:
        status = "Paused"

    status_text = font.render(
        f"Status: {status}",
        True,
        (255,255,255)
    )

    screen.blit(status_text, (250, y+15))
    screen.blit(text, (10, y+15))

###############################################################################################

def draw_button(screen:pygame.Surface, font:pygame.font, text:str, x:float, y:float, width:int, height:int)->pygame.Rect:

    button = pygame.Rect(x,y,width,height)

    pygame.draw.rect(screen, (70,130,180), button)

    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect(center=button.center)

    screen.blit(text_surface, text_rect)

