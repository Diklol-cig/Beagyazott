#!/bin/sh/python3
from sense_hat import SenseHat

sense = SenseHat()

w = (255, 255, 255) # white
b = (255, 0, 0) # red

# Set up how the image look like
smiley_pixels = [
w, w, w, w, w, w, w, w,
w, b, b, w, w, b, b, w,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
w, b, b, b, b, b, b, w,
w, w, b, b, b, b, w, w,
w, w, w, b, b, w, w, w,
w, w, w, w, w, w, w, w]

# change all 64 LEDs
sense.set_pixels(smiley_pixels)