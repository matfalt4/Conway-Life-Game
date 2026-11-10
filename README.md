# Conway's Game of Life

A Python implementation of Conway's Game of Life using Pygame and NumPy.

The project simulates a two-dimensional cellular automaton in which cells evolve according to a set of rules based on the states of their neighbors.

## Technologies

- Python
- Pygame
- NumPy
- unittest (basic tests)

## Features

- Interactive grid with mouse-controlled cell selection
- Simulation based on Conway's Game of Life rules
- Start and pause simulation using the keyboard
- Adjustable simulation update interval
- Resetting the board
- Generation counter
- Separate module for simulation logic

## Game Rules

Each cell can be either alive or dead.

1. A living cell with fewer than two living neighbors dies.
2. A living cell with two or three living neighbors survives.
3. A living cell with more than three living neighbors dies.
4. A dead cell with exactly three living neighbors becomes alive.

Cells outside the grid are treated as dead.

## Project Structure

GameOfLife/
├── main.py
├── game_of_life.py
├── interface.py
└── tests/
    ├── __init__.py
    └── test_game_of_life.py


- main.py — application initialization, event handling and simulation control.
- game_of_life.py — neighbor counting and generation calculations.
- interface.py — graphical interface components (in development).
- tests/ — unit tests for simulation logic.

## Controls

| Key / Action | Function |
|---|---|
| Left mouse button | Toggle cell state |
| Space | Start / pause simulation |
| R | Reset the board |
| Close window | Exit application |

## Installation

Clone the repository and navigate to the project directory.

Install the required libraries:

pip install pygame numpy

Run the application:
python main.py

## Current Status

The project is under development. The core simulation logic and basic keyboard controls have been implemented.

Planned improvements include a dedicated control panel, graphical buttons and further unit tests.
