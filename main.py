import pygame
import numpy as np

from game_of_life import new_generation

pygame.init()
font = pygame.font.Font("Arial",24)

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

simulation_running = False

UPDATE_INTERVAL = 200
last_update = pygame.time.get_ticks()

generation = 0

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
                simulation_running = not simulation_running

            if event.key == pygame.K_r:
                simulation_running = False
                board.fill(0) # NumPy method which fills an entire array with a provided value
                generation = 0


    current_time = pygame.time.get_ticks()

    # This fragment causes that cells are changing its state every 200+ms, (sth. around 5 times per second).
    if simulation_running:
        if current_time - last_update >= UPDATE_INTERVAL:
            board = new_generation(board)
            generation += 1
            last_update = current_time

        
    screen.fill((25,25,25))
    draw_grid(screen)
    text = font.render(f"Generation: {generation}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 

