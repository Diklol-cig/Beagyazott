#!/bin/sh/python3
from sense_hat import SenseHat
from random import randint 
from time import sleep

sense = SenseHat()

# Generate a random color
def random_colour():
# randint - random integer between an interval
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)

sense.show_letter("D", random_colour())
# sleep - temporarily pause your program
sleep(1)
sense.show_letter("A", random_colour())
sleep(1)
sense.show_letter("N", random_colour())
# sleep - temporarily pause your program
sleep(1)
sense.show_letter("I", random_colour())
sleep(1)
sense.clear()
