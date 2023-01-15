import pygame
import sys

from snake_world import SnakeWorld


# Settings
GAME_TITLE = "Snake"
DEFAULT_BACKGROUND = (150, 150, 150)
window_width = 400
window_height = 340
fps = 4

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(GAME_TITLE)
pygame.font.init()
clock = pygame.time.Clock()

# Game objects
snake_world = SnakeWorld()

# Game Loop
while True:

    clock.tick(fps)

    # check for events
    for event in pygame.event.get():

        # quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(DEFAULT_BACKGROUND)

    snake_world.update()
    snake_world.draw(window=window)

    pygame.display.update()
    fps = 4 + snake_world.score * 2
