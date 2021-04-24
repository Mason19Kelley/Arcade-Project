import pygame
import random
from time import sleep
colors = ["red", "blue", "green", "yellow"]
buttons = []
pygame.init()
size = (800, 480)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
class Game:
    def __init__(self, start):
        self.start = start
        self.score = 0
    def play(self):
        b1 = Board(black)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            time = random.randint(0, 3)
            sleep(time)

            # refreshes display each tick
            pygame.display.flip()
            # sets number of ticks per second
            clock.tick(60)

class Board(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

clock = pygame.time.Clock()

