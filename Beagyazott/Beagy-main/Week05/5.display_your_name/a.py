from sense_hat import SenseHat
sense = SenseHat()
from random import randint
from time import sleep
# Generate a random color
def random_colour():
  # randint - random integer between an interval
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)
  
name = "David"
for c in name:
  sense.show_letter(c, random_colour())
  sleep(1)
sense.clear()