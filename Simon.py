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
        self.loc = 2
        self.go = False
    def seqGen(self, cap):
        for i in range(0, cap):
            self.seq.append(randint(0, 3))
    def play(self):
        pygame.display.set_caption("Simon")
        self.simon = pygame.display.set_mode(size)
        self.simon.fill(black)
        pygame.display.update()
        j = 3
        self.seqGen(j)
        while self.state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    return
            print(self.seq)
            if self.go == False:
                for i in range(0, len(self.seq)):
                    if self.seq[i] == 0:
                        sounds[0].play()
                        self.simon.fill(red)
                        sleep(0.1)
                        pygame.display.update()
                        self.simon.fill(black)
                        sleep(1)
                        pygame.display.update()

                    elif self.seq[i] == 1:
                        sounds[1].play()
                        self.simon.fill(green)
                        sleep(0.1)
                        pygame.display.update()
                        self.simon.fill(black)
                        sleep(1)
                        pygame.display.update()

                    elif self.seq[i] == 2:
                        sounds[2].play()
                        self.simon.fill(yellow)
                        sleep(0.1)
                        pygame.display.update()
                        self.simon.fill(black)
                        sleep(1)
                        pygame.display.update()

                    elif self.seq[i] == 3:
                        sounds[3].play()
                        self.simon.fill(blue)
                        sleep(0.1)
                        pygame.display.update()
                        self.simon.fill(black)
                        sleep(1)
                        pygame.display.update()
            self.go == True
                    #code that plays sequence
            while len(self.player_seq) < len(self.seq):
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_z]:
                    self.player_seq.append(0)
                    sounds[0].play()
                    self.simon.fill(red)
                    sleep(0.1)
                    pygame.display.update()
                    self.simon.fill(black)
                    sleep(1)
                    pygame.display.update()
                    self.loc += 1
                if pressed_keys[pygame.K_x]:
                    self.player_seq.append(1)
                    sounds[1].play()
                    self.simon.fill(green)
                    sleep(0.1)
                    pygame.display.update()
                    self.simon.fill(black)
                    sleep(1)
                    pygame.display.update()
                    self.loc += 1
                if pressed_keys[pygame.K_c]:
                    self.player_seq.append(2)
                    sounds[2].play()
                    self.simon.fill(yellow)
                    sleep(0.1)
                    pygame.display.update()
                    self.simon.fill(black)
                    sleep(1)
                    pygame.display.update()
                    self.loc += 1
                if pressed_keys[pygame.K_v]:
                    self.player_seq.append(3)
                    sounds[3].play()
                    self.simon.fill(blue)
                    sleep(0.1)
                    pygame.display.update()
                    self.simon.fill(black)
                    sleep(1)
                    pygame.display.update()
                    self.loc += 1
                if self.player_seq != self.seq[0:self.loc]:
                    self.game_over()
            if self.player_seq == self.seq:
                self.go == False
                self.player_seq = []
                self.seq.append(randint(0,3))
            pygame.display.flip()

            clock.tick(60)
    def game_over(self):
        pass

    def restart(self):
        pass

s1 = Simon()
s1.play()




