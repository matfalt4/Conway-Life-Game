import pygame
import numpy as np

from game_of_life import new_generation

pygame.init()

CELL_SIZE = 20
ROWS = 30
COLS = 40

WIDTH = COLS*CELL_SIZE
HEIGHT = ROWS*CELL_SIZE

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

board = np.zeros((ROWS,COLS), dtype=int)


def draw_grid(screen):

    for rows in range(ROWS):
        for cols in range(COLS):

            x = cols*CELL_SIZE
            y = rows*CELL_SIZE

            if board[rows, cols] == 1:
                
                pygame.draw.rect(
                    screen,
                    (0, 200, 100),
                    (x,y,CELL_SIZE,CELL_SIZE)
                )

            pygame.draw.rect(screen, (80, 80, 80), (x,y,CELL_SIZE,CELL_SIZE), 1)


running = True
clock = pygame.time.Clock()

# Loop used for current service and content refreshing
while running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos

                col = x//CELL_SIZE
                row = y//CELL_SIZE

                board[row, col] = 1-board[row, col]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                board = new_generation(board)

    screen.fill((25,25,25))

    draw_grid(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 

