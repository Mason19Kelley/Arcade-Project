#Main GUI setup for menu

from tkinter import *
import pyglet
pyglet.font.add_file('ARCADECLASSIC.TTF')
class MenuScreen(Frame):
    def __init__(self, container):
        Frame.__init__(self, container)
        self.menuSet()
    def menuSet(self):
        self.display = Label(self, text = "Memory", font =("ARCADECLASSIC", 25), height = 2, width = 15, anchor = 'center', bg = "white")
        self.display.grid(row = 0, column = 0, columnspan = 1)
        self.display = Label(self, text = "Pong", font =("ARCADECLASSIC", 25), height = 2, width = 15, anchor = 'center', bg = "white")
        self.display.grid(row = 0, column = 1, columnspan = 1)
        self.display = Label(self, text = "Speed", font =("ARCADECLASSIC", 25), height = 2, width = 15, anchor = 'center', bg = "white")
        self.display.grid(row = 0, column = 2, columnspan = 1)
        img = PhotoImage(file = "menuIMG/MEMORY.gif")
        self.display = Label(self, image = img, height = 150, width = 266, anchor = 'center', bg = "white")
        self.display.image = img
        self.display.grid(row = 1, column = 0)
        img = PhotoImage(file = "menuIMG/PONG.gif")
        self.display = Label(self, image = img, height = 150, width = 266, anchor = 'center', bg = "white")
        self.display.image = img
        self.display.grid(row = 1, column = 1)
#        self.display = Label(self, img = , height = 2, width = 15, anchor = E, bg = "white")
#        self.display.grid(row = 0, column = 0, columnspan = 6)
        self.pack()
window = Tk()
window.title("Arcade")
WIDTH = 800
HEIGHT = 480
window.geometry("{}x{}".format(WIDTH, HEIGHT))
a1 = MenuScreen(window)
window.mainloop()