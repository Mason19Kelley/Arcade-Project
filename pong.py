#import statements
import pygame
from random import randint, choice
import pyglet
import RPI.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
leds = [5, 24, 26, 12, 16]
switches = [4, 25, 27, 6, 13]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for i in leds:
    GPIO.output(leds, True)
def in_pong(ArtI):
    pyglet.font.add_file('ARCADECLASSIC.TTF')
    #initializes pygame
    pygame.init()

    #base colors for background and sprites
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    #creates a pygame window
    size = (800, 480)

    boop = pygame.mixer.Sound("pong_bounce.wav")
    pygame.mixer.music.load('pong_bounce.wav')


    class Game:
        def __init__(self, start):
            self.start = start
            self.score1 = 0
            self.score2 = 0
            self.pause = False
            self.over = False
            self.winner = None
            self.screen = None
        def play(self, ai):
            player2.AI = ai
            pygame.display.set_caption("Pong")
            self.screen = pygame.display.set_mode(size)
            self.over = False
            previous_key_p = False
            while self.start:
                # quits if x is pressed
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        self.__del__()
                        return
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_p] and previous_key_p == False:
                    self.pauseMenu()
                if pressed_keys[pygame.K_d] and self.pause == True:
                    self.restart()
                if pressed_keys[pygame.K_v] and self.pause == True:
                    pygame.quit()
                    self.__del__()
                    return
                previous_key_p = pressed_keys[pygame.K_p]
                if self.pause == False:
                    # creates list of pressed keys and using that to determine movement
                    pressed_keys = pygame.key.get_pressed()
                    if GPIO.input(switches[0]) == True:
                        player1.moveUp(5)
                    if GPIO.input(switches[3]) == True:
                        player1.moveDown(5)
                    if player2.AI == True:
                        player2.AI_move(ball)
                    else:
                        if GPIO.input(switches[1]) == True:
                            player2.moveUp(5)
                        if GPIO.input(switches[2]) == True:
                            player2.moveDown(5)


                    # scoring system if ball touches variable, increments score and resets ball to middle
                    if ball.rect.x >= 790:
                        self.score1 += 1
                        ball.rect.x = 400
                        ball.rect.y = 240
                        ball.x_velo = choice([-2, 2])
                        ball.y_velo = choice([-1, -2, 1, 2])
                    if ball.rect.x <= 0:
                        self.score2 += 1
                        ball.rect.x = 400
                        ball.rect.y = 240
                        ball.x_velo = choice([-2, 2])
                        ball.y_velo = choice([-1, -2, 1, 2])

                    # bounces ball of top or bottom wall
                    if ball.rect.y > 470 or ball.rect.y < 0:
                        ball.y_velo = -ball.y_velo

                    # detects collision and reflects ball off board
                    if pygame.sprite.collide_mask(ball, player1) or pygame.sprite.collide_mask(ball, player2):
                        ball.bounce()

                    # refresh method to move ball
                    ball.refresh()
                    # draws background and sprites onto screen each tick
                    self.screen.fill(BLACK)
                    pygame.draw.line(self.screen, WHITE, [400, 0], [400, 580], 1)
                    all_sprites_list.update()
                    all_sprites_list.draw(self.screen)

                    # draws score at top
                    font2 = pygame.font.Font('ARCADECLASSIC.TTF', 74)
                    text = font2.render(str(self.score1), 1, BLUE)
                    self.screen.blit(text, (300, 10))
                    text = font2.render(str(self.score2), 1, BLUE)
                    self.screen.blit(text, (470, 10))
                    if self.score1 >= 5:
                        self.victory("Player 1")
                    elif self.score2 >= 5:
                        self.victory("Player 2")
                    # refreshes display each tick
                    pygame.display.flip()
                    # sets number of ticks per second
                    clock.tick(60)
                if self.over == True:
                    self.pause = True
                    self.menu(f"    {self.winner} wins!   ", "Press  R  to restart", "Press  Q  to quit")



        def victory(self, winner):
            self.winner = winner
            self.over = True

        def menu(self, text, text1, text2):
            x = 100
            y = 100
            pygame.draw.rect(self.screen, BLACK, (x, y, 600, 600), 0)
            pygame.draw.rect(self.screen, WHITE, (x - 1, y - 1, 600, 300), 1)
            pygame.draw.rect(self.screen, WHITE, (x - 2, y - 2, 600, 300), 1)
            pygame.draw.rect(self.screen, WHITE, (x - 3, y - 3, 600, 300), 1)
            pygame.draw.rect(self.screen, WHITE, (x - 4, y - 4, 600, 300), 1)
            font = pygame.font.Font('ARCADECLASSIC.TTF', 66)
            text3 = font.render(str(text), 1, RED)
            text4 = font.render(str(text1), 1, RED)
            text5 = font.render(str(text2), 1, RED)
            self.screen.blit(text3, (108,100))
            self.screen.blit(text4, (112, 200))
            self.screen.blit(text5, (164, 300))
            pygame.display.update()
        def pauseMenu(self):
            self.pause = not self.pause
            self.menu("Press P  to  unpause", "Press  R  to restart", "Press  Q  to quit")
        def restart(self):
            self.pause = False
            self.score1 = 0
            self.score2 = 0
            self.over = False
            self.winner = None
            player1.rect.x = 30
            player1.rect.y = 182
            player2.rect.x = 760
            player2.rect.y = 182
            ball.rect.x = 400
            ball.rect.y = 240
            ball.x_velo = choice([-2, 2])
            ball.y_velo = choice([-1, -2, 1, 2])

        def __del__(self):
            del self
    #board class inherits from pygame sprite class
    class Board(pygame.sprite.Sprite):
        #constructor
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)
            self.AI = False
            self.AISpeed = 2.5

            #draws sprite
            pygame.draw.rect(self.image, color, [0, 0, width, height])

            self.rect = self.image.get_rect()

        #moves sprite up
        def moveUp(self, pixels):
             self.rect.y -= pixels
             if self.rect.y < 0:
                self.rect.y = 0
        #moves sprite down
        def moveDown(self, pixels):
            self.rect.y += pixels
            if self.rect.y > 380:
                 self.rect.y = 380

        def AI_move(self, ball):
            if ball.rect.y > self.rect.y:
                self.AISpeed = ((ball.rect.y-self.rect.y))/(15+600/(ball.rect.x+1))
            elif ball.rect.y < self.rect.y:
                self.AISpeed = ((ball.rect.y - self.rect.y))/(15+600/(ball.rect.x+1))

            self.rect.y += self.AISpeed

            if self.rect.y > 380:
                self.rect.y = 380
            if self.rect.y < 0:
                self.rect.y = 0

    #ball class
    class Ball(pygame.sprite.Sprite):
        #class variables: x and y velo
        x_velo = choice([-2,2])
        y_velo = choice([-1,-2,1,2])
        #constructor
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)

            pygame.draw.rect(self.image, color, [0, 0, width, height])

            self.rect = self.image.get_rect()
        #method responsible for moving the ball
        def refresh(self):
            self.rect.x += self.x_velo
            self.rect.y += self.y_velo

        #bounce method for collision with paddle
        def bounce(self):
            self.x_velo = -self.x_velo
            self.y_velo = randint(-8,8)
            boop.play()



    #player 1 instanciating
    player1 = Board(WHITE, 10, 100)
    player1.rect.x = 30
    player1.rect.y = 182

    #player 2 instanciating
    player2 = Board(WHITE, 10, 100)
    player2.rect.x = 760
    player2.rect.y = 182
    player2.AI = True

    #ball instanciation
    ball = Ball(WHITE, 7, 7)
    ball.rect.x = 400
    ball.rect.y = 240

    #initializes list of sprites and adds all instances to it
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player1)
    all_sprites_list.add(player2)
    all_sprites_list.add(ball)


    clock = pygame.time.Clock()
    #initial player scores
    def pong_play(AI):
        game = Game(True)
        game.play(AI)

    pong_play(ArtI)
