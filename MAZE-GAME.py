import pygame as pg
from pygame.locals import *
import random
import sys


# Global Settings
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 900


class MazeGenerator:
    def __init__(self):
        # Need to initialize pygame before using it
        pg.init()

        # Create a display surface to draw my game on
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Set the title on the window
        pg.display.set_caption("The Maze")

    def generate_maze(self):
        pass

    def run_game(self):
        # Main game loop
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            pg.draw.rect(self.screen, (255, 255, 255), (50, 50, 20, 20))
            pg.display.update()

        pg.quit()


mg = MazeGenerator()
mg.run_game()




