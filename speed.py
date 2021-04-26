import pygame
import random
from time import sleep, time
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
        self.scores = 0
        self.state = True
        self.speed = None
        self.val = None
        self.t = None
        self.times = 10
    def game_over(self):
        pygame.draw.rect(self.speed, black, (10, 10, 780, 460))
        # font = pygame.font.Font('ARCADECLASSIC.TTF', 50)
        # text = font.render("You Failed\nScore: {}".format(self.score), 1, white)
        # self.speed.blit(text, (300, 160))
    def speedPlay(self):
        pygame.init()
        pygame.display.set_caption("Speed")
        self.speed = pygame.display.set_mode(size)
        self.speed.fill(black)
        self.t = random.randint(0,3)
        pygame.display.update()
        while self.state and self.times > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    return
            self.speed.fill(colors[self.t])
            font2 = pygame.font.Font('ARCADECLASSIC.TTF', 74)
            text = font2.render(str(self.times), 1, white)
            self.speed.blit(text, (20, 10))
            start = timeit.timeit()
            start_time = time()
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            text = myfont.render(str(time()-start_time), 1, black)
            self.speed.blit(text, (100, 100))
            pygame.display.update()
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

            if self.pressed == True:
                    if self.val == self.t:
                        end = timeit.timeit() - start
                        self.t = random.randint(0, 3)
                        self.speed.fill(black)
                        pygame.display.update()
                        self.pressed = False
                        self.times -= 1
                        sleep(1)


            # refreshes display each tick
            pygame.display.flip()
            # sets number of ticks per second
            clock.tick(60)
s1 = SpeedGame()
clock = pygame.time.Clock()
s1.speedPlay()





