import pygame
import random
from time import sleep
#import RPi.GPIO as GPIO
import timeit
import pyglet
pyglet.font.add_file('ARCADECLASSIC.TTF')
buttons = []
size = (800, 480)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
colors = [red, blue, green, yellow]
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
class SpeedGame:
    def __init__(self):
        self.pressed = False
        self.score = 0
        self.state = True
        self.speed = None
        self.val = None
        self.t = None
    def loss(self):
        pygame.draw.rect(self.speed, black, (10, 10, 780, 460))
        font = pygame.font.Font('ARCADECLASSIC.TTF', 50)
        text = font.render("You Failed\nScore: {}".format(self.score), 1, white)
        self.speed.screen.blit(text, (300, 160))
    def speedPlay(self):
        pygame.init()
        pygame.display.set_caption("Speed")
        self.speed = pygame.display.set_mode(size)
        self.speed.fill(red)
        self.t = random.randint(0,3)
        pygame.display.update()
        while self.state:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            #pygame.draw.rect(self.speed, colors[t], (10, 10, 780, 460))
            self.speed.fill(colors[self.t])
            start = timeit.timeit()
            while not self.pressed:
                for i in range(len(buttons)):
                    if GPIO.input(buttons[i]) == True:
                        self.val = i
                        self.pressed = True
            if self.val == self.t:
                end = timeit.timeit() - start
                self.score += 1
                self.t = random.randint(0, 3)
            else:
                self.loss()

            # refreshes display each tick
            pygame.display.flip()
            # sets number of ticks per second
            clock.tick(60)
s1 = SpeedGame()
clock = pygame.time.Clock()
s1.speedPlay()





