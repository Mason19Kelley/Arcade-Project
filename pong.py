#import statements
import pygame
from random import randint, choice

#initializes pygame
pygame.init()

#base colors for background and sprites
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#creates a pygame window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#board class inherits from pygame sprite class
class Board(pygame.sprite.Sprite):
    #constructor
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

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
        if self.rect.y > 400:
             self.rect.y = 400

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


#player 1 instanciating
player1 = Board(WHITE, 10, 100)
player1.rect.x = 30
player1.rect.y = 190

#player 2 instanciating
player2 = Board(WHITE, 10, 100)
player2.rect.x = 670
player2.rect.y = 190

#ball instanciation
ball = Ball(WHITE, 7, 7)
ball.rect.x = 350
ball.rect.y = 250

#initializes list of sprites and adds all instances to it
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(ball)


play = True
clock = pygame.time.Clock()

#initial player scores
score1 = 0
score2 = 0

#main program loop
while play:
    #quits if x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #creates list of pressed keys and using that to determine movement
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        player1.moveUp(5)
    if pressed_keys[pygame.K_s]:
        player1.moveDown(5)
    if pressed_keys[pygame.K_UP]:
        player2.moveUp(5)
    if pressed_keys[pygame.K_DOWN]:
        player2.moveDown(5)

    #scoring system if ball touches variable, increments score and resets ball to middle
    if ball.rect.x >= 690:
        score1 += 1
        ball.rect.x = 350
        ball.rect.y = 250
        ball.x_velo = choice([-2, 2])
        ball.y_velo = choice([-1, -2, 1, 2])
    if ball.rect.x <= 0:
        score2 += 1
        ball.rect.x = 350
        ball.rect.y = 250
        ball.x_velo = choice([-2, 2])
        ball.y_velo = choice([-1, -2, 1, 2])

    #bounces ball of top or bottom wall
    if ball.rect.y >490 or ball.rect.y<0:
        ball.y_velo = -ball.y_velo

    #detects collision and reflects ball off board
    if pygame.sprite.collide_mask(ball, player1) or pygame.sprite.collide_mask(ball, player2):
      ball.bounce()


    #refresh method to move ball
    ball.refresh()
    #draws background and sprites onto screen each tick
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 1)
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    #draws score at top
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(score2), 1, WHITE)
    screen.blit(text, (420,10))

    #refreshes display each tick
    pygame.display.flip()
    #sets number of ticks per second
    clock.tick(60)
