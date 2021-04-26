import pygame
import random
from time import sleep
#import RPi.GPIO as GPIO
import timeit
import pyglet
pyglet.font.add_file('ARCADECLASSIC.TTF')
buttons = [0,1,2,3]
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
        self.speed.blit(text, (300, 160))
    def speedPlay(self):
        pygame.init()
        pygame.display.set_caption("Speed")
        self.speed = pygame.display.set_mode(size)
        self.speed.fill(red)
        self.t = random.randint(0,3)
        pygame.display.update()
        while self.state:
            print(self.t)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.speed.fill(colors[self.t])
            print('HI')
            start = timeit.timeit()
            pygame.display.update()
            while not self.pressed:

                for i in range(len(buttons)):
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[pygame.K_0] == True:
                        self.val = 0
                        self.pressed = True
                    elif pressed_keys[pygame.K_1] == True:
                        self.val = 1
                        self.pressed = True
                    elif pressed_keys[pygame.K_2] == True:
                        self.val = 2
                        self.pressed = True
                    elif pressed_keys[pygame.K_3] == True:
                        self.val = 3
                        self.pressed = True

            if self.val == self.t:
                end = timeit.timeit() - start
                self.score += 1
                self.t = random.randint(0, 3)
                sleep(1)
            else:
                self.loss()

            # refreshes display each tick
            pygame.display.flip()
            # sets number of ticks per second
            clock.tick(60)
s1 = SpeedGame()
clock = pygame.time.Clock()
s1.speedPlay()





