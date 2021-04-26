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
state = True
score = 0
pressed = False
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def loss():
    pygame.draw.rect(Speed, black, (10, 10, 780, 460))
    font = pygame.font.Font('ARCADECLASSIC.TTF', 50)
    text = font.render("You Failed\nScore: {}".format(score), 1, WHITE)
    Speed.screen.blit(text, (300, 160))
def speedPlay():
    pygame.init()
    Speed = pygame.display.set_mode((size), 0, 32)
    pygame.display.set_caption("Speed")
    Speed.fill(0,0,0)
    t = randint(0,3)
    while state:
        pygame.draw.rect(Speed, colors[t], (10, 10, 780, 460))
        start = timeit.timeit()
        while not pressed:
            for i in range(len(buttons)):
                if GPIO.input(buttons[i]) == True:
                    val = i
                    pressed = True
        if val == t:
            end = timeit.timeit() - start
            score += 1
            t = randint(0, 3)
        else:
            loss()
speedPlay()
loss()





