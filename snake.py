import pygame
import random


pygame.init()

class SnakeGame:

    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock

        # init game state
        self.direction = ""

    def play_step(self):
        pass

if __name__ == '__main__':
    game = SnakeGame()

    # game loop
    while True:
        game.play_step()

        # break if game over



    pygame.quit()