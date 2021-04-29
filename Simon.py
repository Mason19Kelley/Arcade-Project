
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

size = (800, 480)
red = (255,0,0)
blue = (0,0,255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0,0,0)
white = (255,255,255)
sounds = [pygame.mixer.Sound("do.wav"),pygame.mixer.Sound("re.wav"), pygame.mixer.Sound("sol.wav"),pygame.mixer.Sound("fa.wav")]

class Simon:
    def __init__(self):
        self.state = True
        self.seq = []
        self.screen = None
        self.score = 0
    def play(self):
        pass



