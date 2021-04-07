#arcade project
from tkinter import *
import pyglet
from random import randint, choice
import pygame
pyglet.font.add_file('ARCADECLASSIC.TTF')

WIDTH = 800
HEIGHT = 480

window = Tk()
window.title("Arcade Project")
window.geometry("800x480")
window.configure(bg="black")

title = Label(text="Triple Arcade Madness", anchor=N, font=("ARCADECLASSIC", 50), foreground="Blue", bg="black")
game1 = Button(text="Simon  Says", bg ="white", font=("ARCADECLASSIC", 20)).place(x=110, y=400)
game2 = Button(text="Reaction   Test", bg ="white", font=("ARCADECLASSIC", 20)).place(x=320, y=400)
game3 = Button(text="Pong", bg ="white", font=("ARCADECLASSIC", 20)).place(x=600, y=400)
# game1.pack(side=BOTTOM)
# game2.pack(side=BOTTOM)
# game3.pack(side=BOTTOM)
title.pack()


window.mainloop()
