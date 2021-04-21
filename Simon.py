    #######################################
#Name: Jordan Hartung
#Date: 02-27-2021
#Desc: its the Pimon game(get it) hehe
#######################################


import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame
from tkinter import *

#Set true for debug 
DEBUG = False

pygame.init()

#all assets used by GPIO
switches = [20, 16, 12, 26]
leds = [6, 13, 19, 21]
sounds = [pygame.mixer.Sound("one.wav"),pygame.mixer.Sound("two.wav"), pygame.mixer.Sound("three.wav"),pygame.mixer.Sound("four.wav")]
#GPIO ESTABLISHMENT
GPIO.setmode(GPIO.BCM)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)
#function to power all LEDS
def all_on():
    for i in leds:
        GPIO.output(leds, True)
#function to turn off all LEDS
def all_off():
    for i in leds:
        GPIO.output(leds, False)
#Funtion to display that user has lost 
def lose():
    for i in range(0, 4):
        all_on()
        sleep(0.5)
        all_off()
        sleep(0.5)
# Game code
seq = []
#Generates Starting sequence
seq.append(randint(0,3))
seq.append(randint(0,3))

print("Welcome to Simon!")
print("Try to play the sequence back by pressing the switches.")
print("Press Ctrl+C to exit...")

#initiates all game unless keyboard press happens
def Splay():
    try:
        while True:
            seq.append(randint(0,3))
            if DEBUG:
                if len(seq) > 3:
                    print()
                print("seq={}".format(seq))
            #lights and plays sounds in respect to randomly generated sequence
            for s in seq:
                if(len(seq)>=15):
                    GPIO.output(leds[s], False)
                    sounds[s].play()
                    sleep(0.6)
                elif(len(seq)>=13):
                    GPIO.output(leds[s], True)
                    sounds[s].play()
                    sleep(0.6)
                    GPIO.output(leds[s], False)
                    sleep(0.15)

                elif(len(seq)>=10):
                    GPIO.output(leds[s], True)
                    sounds[s].play()
                    sleep(0.7)
                    GPIO.output(leds[s], False)
                    sleep(0.25)

                elif(len(seq)>=7):
                    GPIO.output(leds[s], True)
                    sounds[s].play()
                    sleep(0.8)
                    GPIO.output(leds[s], False)
                    sleep(0.3)

                elif(len(seq)>=5):
                    GPIO.output(leds[s], True)
                    sounds[s].play()
                    sleep(0.9)
                    GPIO.output(leds[s], False)
                    sleep(0.4)

                else:
                    GPIO.output(leds[s], True)
                    sounds[s].play()
                    sleep(1)
                    GPIO.output(leds[s], False)
                    sleep(0.5)

            switch_count = 0
            #Records and compares pressed switch sequence to random seqeunce
            while switch_count < len(seq):
                pressed = False
                while(not pressed):
                    for i in range(len(switches)):
                        while(GPIO.input(switches[i])== True):
                            val = i
                            pressed= True
                if DEBUG:
                    print(val)
                GPIO.output(leds[val], True)
                sounds[val].play()
                sleep(1)
                GPIO.output(leds[val], False)
                sleep(0.25)
                #losing outcome if sequences don't match
                if (val != seq[switch_count]):
                    lose()
                    if(len(seq) > 3):
                        print("You made it to a sequence of {}!".format(len(seq)))
                    else:
                        print("You didn't even make it to a sequence!")
                    GPIO.cleanup()
                    exit(0)
                switch_count+=1
#ends game and cleans GPIO on keyboard interruption
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(0)


