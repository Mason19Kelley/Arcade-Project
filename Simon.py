from random import randint
import pygame
import pyglet
from time import sleep

pyglet.font.add_file('ARCADECLASSIC.TTF')
pygame.init()

size = (800, 480)
red = (255,0,0)
blue = (0,0,255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0,0,0)
white = (255,255,255)
sounds = [pygame.mixer.Sound("do.wav"),pygame.mixer.Sound("re.wav"), pygame.mixer.Sound("sol.wav"),pygame.mixer.Sound("fa.wav")]

clock = pygame.time.Clock()

class Simon:
    def __init__(self):
        self.state = True
        self.simon = None
        self.seq = []
        self.screen = None
        self.score = 0
        self.player_seq = []
        self.loc = 0
    def play(self):
        pygame.display.set_caption("Simon")
        self.simon = pygame.display.set_mode(size)
        self.simon.fill(black)
        pygame.display.update()
        while self.state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    return
            self.seq  += randint(0,3)
            for i in self.seq:
                #code that plays sequence
                sleep(.5)
            while len(self.player_seq) < len(self.seq):
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_z]:
                    self.loc += 1
                if pressed_keys[pygame.K_x]:
                    self.loc += 1
                if pressed_keys[pygame.K_c]:
                    self.loc += 1
                if pressed_keys[pygame.K_v]:
                    self.loc += 1
                if self.player_seq != self.seq[0:self.loc]:
                    self.game_over()
            pygame.display.flip()

            clock.tick(60)
    def game_over(self):
        pass

    def restart(self):
        pass

s1 = Simon()
s1.play()




