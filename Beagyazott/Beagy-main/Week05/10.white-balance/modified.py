from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

# Define the functions
def red():
  while True:
    w = (0, 0, 0) # black
    r = (255,0,0)
    # Set up how the image look like
    smiley_pixels = [
     w, w, w, w, w, w, w, w,
     w, r, r, w, w, r, r, w,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     w, r, r, r, r, r, r, w,
     w, w, r, r, r, r, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, w, w, w, w, w]
     
    # change all 64 LEDs
    sense.set_pixels(smiley_pixels)
    sleep(1)
    sense.clear()
    sleep(1)
    
def blue():
  sense.clear(0, 0, 255)
def green():
  sense.clear(0, 255, 0)
def yellow():
  sense.clear(255, 255, 0)
  
sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear
while True:
  # do nothing
  pass