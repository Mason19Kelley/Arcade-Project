#Main GUI setup for menu

from tkinter import *
import pyglet
import pong
import pygame
import speed
import Simon
import RPi.GPIO as GPIO
pyglet.font.add_file('ARCADECLASSIC.TTF')
pygame.init()
for i in leds:
    GPIO.output(leds, True)

class MenuScreen(Frame, Canvas):
    def __init__(self, container):
        Frame.__init__(self, container)
        self.menuSet()
    def menuSet(self):
        bg = PhotoImage(file="menuIMG/mario.gif")
        back = Label(self, width = WIDTH, height = HEIGHT, image = bg)
        back.image = bg
        back.place(x = 0, y= 0, relwidth = 1, relheight = 1)
        self.display = Label(self, text = "Memory", font =("ARCADECLASSIC", 25), height = 2, width = 15, anchor = 'center')
        self.display.grid(row = 0, column = 0)
        self.display = Label(self, text = "Pong", font =("ARCADECLASSIC", 25), height = 2, width = 15, anchor = 'center')
        self.display.grid(row = 0, column = 1)
        self.display = Label(self, text = "Speed", font =("ARCADECLASSIC", 25), height = 2, width = 15, anchor = 'center')
        self.display.grid(row = 0, column = 2)
        img = PhotoImage(file = "menuIMG/MEMORY.gif")
        self.display = Label(self, image = img, height = 245, width = 272, anchor = 'center', bg = 'deep sky blue')
        self.display.image = img
        self.display.grid(row = 1, column = 0)
        img = PhotoImage(file = "menuIMG/PONG.gif")
        self.display = Label(self, image = img, height = 245, width = 272, anchor = 'center', bg = 'deep sky blue')
        self.display.image = img
        self.display.grid(row = 1, column = 1)
        img = PhotoImage(file = "menuIMG/lpr.gif")
        self.display = Label(self, image = img , height = 245, width = 272, anchor = 'center', bg = 'deep sky blue')
        self.display.image = img
        self.display.grid(row = 1, column = 2)
        button = Button(self, text = "Start", font = ('ARCADECLASSIC', 15), height = 2, width = 15, anchor = 'center', bg = 'white', command = lambda: Simon.in_simon())
        button.grid(row = 2, column = 0)
        button = Button(self, text = "One\nPlayer", font = ('ARCADECLASSIC', 15), height = 2, width = 15, anchor = 'center', bg = 'white', command= lambda: pong.in_pong(True))
        button.grid(row = 2, column = 1)
        button = Button(self, text = "Two\nPlayers", font = ('ARCADECLASSIC', 15), height = 2, width = 15, anchor = 'center', bg = 'white', command = lambda: pong.in_pong(False))
        button.grid(row = 3, column = 1)
        button = Button(self, text = "Start", font = ('ARCADECLASSIC', 15), height = 2, width = 15, anchor = 'center', bg = 'white', command = lambda: speed.in_speed())
        button.grid(row = 2, column = 2)
        self.pack(fill = "both", expand = True)

    def pongMenu(self):
        pass

window = Tk()
window.title("Arcade")
WIDTH = 800
HEIGHT = 480
window.geometry("{}x{}".format(WIDTH, HEIGHT))
a1 = MenuScreen(window)

window.mainloop()