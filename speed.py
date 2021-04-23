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
        while True:
            time = random.randint(0, 3)
            sleep(time)

class Board(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()



