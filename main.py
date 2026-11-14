import pygame
import numpy as np

from game_of_life import new_generation

form interface import draw_grid, draw_panel, draw_button

pygame.init()
font = pygame.font.Font("Arial",24)

CELL_SIZE = 20
ROWS = 30
COLS = 40

PANEL_HEIGHT = 60
WIDTH = COLS*CELL_SIZE
HEIGHT = ROWS*CELL_SIZE + PANEL_HEIGHT

BUTTON_X = 500
BUTTON_Y = ROWS*CELL_SIZE
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 40

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

start_button = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

board = np.zeros((ROWS,COLS), dtype=int)

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
                x,y = pygame.mouse.get_pos()

                col = x//CELL_SIZE
                row = y//CELL_SIZE

                if 0 <= col < COLS and 0 <= row < ROWS:
                    board[row, col] = 1-board[row, col]

            if start_button.collidepoint(event.pos):
                simulation_running = not simulation_running

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                simulation_running = not simulation_running

            if event.key == pygame.K_r:
                simulation_running = False
                board.fill(0) # NumPy method which fills an entire array with a provided value
                generation = 0


    if simulation_running = True:
        text_str = "STOP"
    else:
        text_str = "START"
        
    current_time = pygame.time.get_ticks()

    # This fragment causes that cells are changing its state every 200+ms, (sth. around 5 times per second).
    if simulation_running:
        if current_time - last_update >= UPDATE_INTERVAL:
            board = new_generation(board)
            generation += 1
            last_update = current_time

        
    screen.fill((25,25,25))
    draw_grid(screen, board, CELL_SIZE)
    draw_panel(screen, ROWS, CELL_SIZE, PANEL_HEIGHT, generation, font)
    draw_button(screen,font,text_str,BUTTON_X,BUTTON_Y,BUTTON_WIDTH,BUTTON_HEIGHT)

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 

