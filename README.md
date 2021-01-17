# Alien Invasion
Alien Invasion is a 2D game based on PyGame, from the book Python Crash Course.

## Dependencies
- python 3
- pip
- pygame

## Installation
### Linux
`pip3 install pygame`

### Windows
`pip -m install pygame`

## Usage
Start the game by running `alien_invasion.py` from a command line:
- `python alien_invasion.py` (Windows)
- `python3 alien_invasion.py` (Linux)

## Playing the game
The goal is to shoot down the alien fleet with your space ship.
- You start with 3 lives displayed on the top left of the screen
- Your current score is displayed on the top right of the screen
- The high score in the current session is displayed in the top center of the screen
- Your ship can move left and right using the `LEFT ARROW KEY` and `RIGHT ARROW KEY` respectively
- You can shoot bullets using the `Spacebar`
- When you shoot the whole fleet, a new one is created. The game levels up and the difficulty increases.
- If you lose all 3 lives, the game ends and your score resets. You can restart again by pressing the `Start the game` button
- You can close the game by pressing `q` or closing the window
