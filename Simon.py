#import statements
from random import randint
import pygame
import pyglet
from time import sleep
import RPi.GPIO as GPIO

#GPIO setup
GPIO.setmode(GPIO.BCM)
switches = [4, 25, 27, 6, 13]
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#play functions
def in_simon():
	#pygame setup
	pyglet.font.add_file('ARCADECLASSIC.TTF')
	pygame.init()

	#base variables
    size = (800, 480)
	red = (255, 0, 0)
	blue = (0, 0, 255)
	green = (0, 255, 0)
	yellow = (255, 255, 0)
	black = (0, 0, 0)
	white = (255, 255, 255)
	sounds = [pygame.mixer.Sound("do.wav"), pygame.mixer.Sound("re.wav"), pygame.mixer.Sound("sol.wav"),
			  pygame.mixer.Sound("fa.wav")]
	clock = pygame.time.Clock()

	#main Simon class
	class Simon:
		#constructor
		def __init__(self):
			self.state = True
			self.simon = None
			self.seq = []
			self.screen = None
			self.score = 0
			self.player_seq = []
			self.play = True
			self.over = False
			self.time = 1

		#generates sequence
		def seqGen(self, cap):
			for i in range(0, cap):
				self.seq.append(randint(0, 3))

		#simon play method
		def Simonplay(self):
			#pygame setup and screen setup
			pygame.display.set_caption("Simon")
			self.simon = pygame.display.set_mode(size)
			self.simon.fill(black)
			pygame.display.update()
			self.seqGen(3)
			#main play loop
			while self.state:
				#quit loop
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.display.quit()
						pygame.quit()
						return
				#quit and restart functions
				if GPIO.input(switches[2]) and self.over == True:
					pygame.quit()
					self.__del__()
					return
				if GPIO.input(switches[4]) and self.over == True:
					self.restart()
				#plays if game is not over
				if self.play == True:
					#sequence play loop
					for i in range(0, len(self.seq)):
						#plays sequence and flashes color based on sequence number
						if self.seq[i] == 0:
							sounds[0].play()
							self.simon.fill(red)
							sleep(0.1)
							pygame.display.update()
							self.simon.fill(black)
							sleep(self.time)
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
					self.play = False
				# player sequence input
				if len(self.player_seq) < len(self.seq) and self.over == False:
					#detects which input it is and add to the player seq var
					if GPIO.input(switches[0]):
						self.player_seq.append(0)
						sounds[0].play()
						self.simon.fill(red)
						sleep(0.1)
						pygame.display.update()
						self.simon.fill(black)
						sleep(1)
						pygame.display.update()
					if GPIO.input(switches[1]):
						self.player_seq.append(1)
						sounds[1].play()
						self.simon.fill(green)
						sleep(0.1)
						pygame.display.update()
						self.simon.fill(black)
						sleep(1)
						pygame.display.update()
					if GPIO.input(switches[2]):
						self.player_seq.append(2)
						sounds[2].play()
						self.simon.fill(yellow)
						sleep(0.1)
						pygame.display.update()
						self.simon.fill(black)
						sleep(1)
						pygame.display.update()
					if GPIO.input(switches[3]):
						self.player_seq.append(3)
						sounds[3].play()
						self.simon.fill(blue)
						sleep(0.1)
						pygame.display.update()
						self.simon.fill(black)
						sleep(1)
						pygame.display.update()
					#exits loop if player seq != seq length
					if self.player_seq != self.seq[0:len(self.player_seq)]:
						self.game_over()
						self.over = True
					#if sequence completed increment and speed up game
					if self.player_seq == self.seq:
						self.score += 1
						if self.time > 0:
							self.time -= .1
						self.play = True
						self.player_seq = []
						self.seq.append(randint(0, 3))
					pygame.display.flip()

				clock.tick(60)
		#game over method
		def game_over(self):
			self.score = len(self.seq) - 3
			self.simon_menu(f"           Final  Score  {self.score}", "Press  WHITE  to restart",
							"Press  YELLOW  to quit")
		#restart method
		def restart(self):
			self.state = True
			self.simon = pygame.display.set_mode(size)
			self.simon.fill(black)
			pygame.display.update()
			self.seq = []
			self.seqGen(3)
			self.screen = None
			self.score = 0
			self.player_seq = []
			self.play = True
			self.over = False
			sleep(1)

		#menu for gameover
		def simon_menu(self, text, text1, text2):
			x = 100
			y = 100
			pygame.draw.rect(self.simon, black, (x, y, 600, 600), 0)
			pygame.draw.rect(self.simon, white, (x - 1, y - 1, 600, 300), 1)
			pygame.draw.rect(self.simon, white, (x - 2, y - 2, 600, 300), 1)
			pygame.draw.rect(self.simon, white, (x - 3, y - 3, 600, 300), 1)
			pygame.draw.rect(self.simon, white, (x - 4, y - 4, 600, 300), 1)
			font = pygame.font.Font('ARCADECLASSIC.TTF', 50)
			text3 = font.render(str(text), 1, red)
			text4 = font.render(str(text1), 1, white)
			text5 = font.render(str(text2), 1, yellow)
			self.simon.blit(text3, (160, 125))
			self.simon.blit(text4, (120, 225))
			self.simon.blit(text5, (160, 325))
			pygame.display.update()

		#delete magic method
		def __del__(self):
			del self

	def play_speed():
		s1 = Simon()
		s1.Simonplay()

	play_speed()