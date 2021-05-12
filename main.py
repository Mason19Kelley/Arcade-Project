# Main GUI setup for menu

from tkinter import *
import pong
import pygame
import speed
import Simon
import RPi.GPIO as GPIO
from time import sleep

pygame.init()
switches = [4, 25, 27, 6, 13]
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class MenuScreen(Frame, Canvas):
	def __init__(self, container):
		Frame.__init__(self, container)
		self.play = False
		self.music = True
		self.commands = [lambda: Simon.in_simon(), lambda: pong.in_pong(True), lambda: pong.in_pong(False),
						 lambda: speed.in_speed()]
		self.button = 0
		self.button0 = None
		self.button1 = None
		self.button2 = None
		self.button3 = None
		self.menuSet()

	def menuSet(self):
		bg = PhotoImage(file="menuIMG/mario.gif")
		back = Label(self, width=WIDTH, height=HEIGHT, image=bg)
		back.image = bg
		back.place(x=0, y=0, relwidth=1, relheight=1)
		self.display = Label(self, text="Memory", font=("ARCADECLASSIC", 25), height=2, width=15, anchor='center')
		self.display.grid(row=0, column=0)
		self.display = Label(self, text="Pong", font=("ARCADECLASSIC", 25), height=2, width=15, anchor='center')
		self.display.grid(row=0, column=1)
		self.display = Label(self, text="Speed", font=("ARCADECLASSIC", 25), height=2, width=15, anchor='center')
		self.display.grid(row=0, column=2)
		img = PhotoImage(file="menuIMG/MEMORY.gif")
		self.display = Label(self, image=img, height=245, width=272, anchor='center', bg='deep sky blue')
		self.display.image = img
		self.display.grid(row=1, column=0)
		img = PhotoImage(file="menuIMG/PONG.gif")
		self.display = Label(self, image=img, height=245, width=272, anchor='center', bg='deep sky blue')
		self.display.image = img
		self.display.grid(row=1, column=1)
		img = PhotoImage(file="menuIMG/lpr.gif")
		self.display = Label(self, image=img, height=245, width=272, anchor='center', bg='deep sky blue')
		self.display.image = img
		self.display.grid(row=1, column=2)
		self.button0 = Button(self, text="Start", font=('ARCADECLASSIC', 15), height=2, width=15, anchor='center',
							  bg='white', command=lambda: Simon.in_simon())
		self.button0.grid(row=3, column=0)
		self.button1 = Button(self, text="One\nPlayer", font=('ARCADECLASSIC', 15), height=2, width=15, anchor='center',
							  bg='white', command=lambda: pong.in_pong(True))
		self.button1.grid(row=3, column=1)
		self.button2 = Button(self, text="Two\nPlayers", font=('ARCADECLASSIC', 15), height=2, width=15,
							  anchor='center', bg='white', command=lambda: pong.in_pong(False))
		self.button2.grid(row=4, column=1)
		self.button3 = Button(self, text="Start", font=('ARCADECLASSIC', 15), height=2, width=15, anchor='center',
							  bg='white', command=lambda: speed.in_speed())
		self.button3.grid(row=3, column=2)
		self.pack(fill="both", expand=True)


window = Tk()
window.title("Arcade")
WIDTH = 800
HEIGHT = 480
window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, 0, 0))
window.attributes('-zoomed', True)
a1 = MenuScreen(window)
while True:
	if a1.play == False:
		if GPIO.input(switches[0]):
			if a1.button == 0:
				a1.button = 3
			else:
				a1.button -= 1
		if GPIO.input(switches[3]):
			print('f')
			if a1.button == 3:
				a1.button = 0
			else:
				a1.button += 1
		if a1.button == 0:
			a1.button0['bg'] = 'red2'
		else:
			a1.button0.config(bg='white')
		if a1.button == 1:
			a1.button1.config(bg='red2')
		else:
			a1.button1.config(bg='white')
		if a1.button == 2:
			a1.button2.config(bg='red2')
		else:
			a1.button2.config(bg='white')
		if a1.button == 3:
			a1.button3.config(bg='red2')
		else:
			a1.button3.config(bg='white')
		sleep(.15)
		if GPIO.input(switches[4]):
			a1.commands[a1.button]()

	a1.update_idletasks()
	a1.update()