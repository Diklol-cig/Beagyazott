from sense_hat import SenseHat
sense = SenseHat()


# Define the functions
def red():
  #set a given color on all LEDs
  sense.clear(255, 0, 0)
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