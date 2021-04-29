from random import randint
import pygame
import pyglet


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

            pygame.display.flip()

            clock.tick(60)


s1=Simon()
s1.play()




