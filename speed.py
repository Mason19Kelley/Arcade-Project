import pygame
import random
from time import sleep
import pyglet
import RPi.GPIO as GPIO

#GPIO setup
GPIO.setmode(GPIO.BCM)
leds = [5, 24, 26, 12, 16]
switches = [4, 25, 27, 6, 13]
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#main play functions
def in_speed():
	#initial variables
	pyglet.font.add_file('ARCADECLASSIC.TTF')
	size = (800, 480)
	red = (255, 0, 0)
	blue = (0, 0, 255)
	green = (0, 255, 0)
	yellow = (255, 255, 0)
	black = (0, 0, 0)
	white = (255, 255, 255)
	colors = [red, green, yellow, blue]
	clock = pygame.time.Clock()

	#speed game class
	class SpeedGame:
		#constructor
		def __init__(self):
			self.pressed = False
			self.scores = []
			self.state = True
			self.speed = None
			self.val = None
			self.t = None
			self.times = 10
			self.time = 0
			self.last = 0
			self.over = False

		#game over functions
		def game_over(self):
			self.speed_menu(f"{sum(self.scores) // len(self.scores)}", "Press  White  to restart",
							"Press  Yellow  to quit")

		#main play function
		def speedPlay(self):
			#pygame and variable initialization
			pygame.init()
			pygame.display.set_caption("Speed")
			self.speed = pygame.display.set_mode(size)
			self.speed.fill(black)
			self.t = random.randint(0, 3)
			self.time = pygame.time.get_ticks()
			self.last = self.time
			pygame.display.update()
			#main play loop
			while self.state:
				#quit game
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.display.quit()
						pygame.quit()
						return
				#ends game is self.over is true
				if self.over == True:
					if GPIO.input(switches[4]):
						self.restart()

					if GPIO.input(switches[2]):
						pygame.quit()
						self.__del__()
						return
				#plays this if there are more times left in the sequence
				if self.times > 0:
					#writes color and timer to screen
					self.speed.fill(colors[self.t])
					font2 = pygame.font.Font('ARCADECLASSIC.TTF', 74)
					text = font2.render(str(self.times), 1, white)
					self.speed.blit(text, (20, 10))
					start = (pygame.time.get_ticks() - self.last)
					font2 = pygame.font.Font('ARCADECLASSIC.TTF', 200)
					text = font2.render(str(start), 1, white)
					self.speed.blit(text, (250, 135))
					pygame.display.update()
					#detects which button is pressed
					if GPIO.input(switches[0]) == True:
						self.val = 0
						self.pressed = True
					elif GPIO.input(switches[1]) == True:
						self.val = 1
						self.pressed = True
					elif GPIO.input(switches[2]) == True:
						self.val = 2
						self.pressed = True
					elif GPIO.input(switches[3]) == True:
						self.val = 3
						self.pressed = True

					#checks if button is the required button to be pressed
					if self.pressed == True:
						if self.val == self.t:
							end = (pygame.time.get_ticks() - self.last)
							self.last += end
							self.last += 1000
							print(start)
							self.scores.append(start)
							self.t = random.randint(0, 3)
							self.speed.fill(black)
							pygame.display.update()
							self.pressed = False
							self.times -= 1
							sleep(1)
				#ends game once sequence is over
				else:
					self.game_over()

				# refreshes display each tick
				pygame.display.flip()
				# sets number of ticks per second
				clock.tick(60)

		#menu for game over
		def speed_menu(self, text, text1, text2):
			x = 100
			y = 100
			pygame.draw.rect(self.speed, black, (x, y, 600, 600), 0)
			pygame.draw.rect(self.speed, white, (x - 1, y - 1, 600, 300), 1)
			pygame.draw.rect(self.speed, white, (x - 2, y - 2, 600, 300), 1)
			pygame.draw.rect(self.speed, white, (x - 3, y - 3, 600, 300), 1)
			pygame.draw.rect(self.speed, white, (x - 4, y - 4, 600, 300), 1)
			font = pygame.font.Font('ARCADECLASSIC.TTF', 50)
			text3 = font.render(str("Score " + text), 1, red)
			text4 = font.render(str(text1), 1, white)
			text5 = font.render(str(text2), 1, yellow)
			if sum(self.scores) // len(self.scores) > 1000:
				self.speed.blit(text3, (267, 125))
			elif sum(self.scores) // len(self.scores) > 10000:
				self.speed.blit(text3, (200, 125))
			else:
				self.speed.blit(text3, (280, 125))
			self.speed.blit(text4, (122, 225))
			self.speed.blit(text5, (150, 325))
			self.over = True
			pygame.display.update()

		#restart method
		def restart(self):
			self.pressed = False
			self.scores = []
			self.state = True
			self.val = None
			self.t = random.randint(0, 3)
			self.times = 10
			self.time = pygame.time.get_ticks()
			self.last = self.time
			self.over = False
			pygame.display.update()
		#delete method
		def __del__(self):
			del self

	#play method
	def play_speed():
		s1 = SpeedGame()
		s1.speedPlay()

	play_speed()
