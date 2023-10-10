from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

while True:
  #go throw all joystick’s events
  for event in sense.stick.get_events():
  # Check if the joystick was pressed
    if event.action == "pressed":
      # Check which direction
      if event.direction == "up":
        sense.show_letter("U") # Up arrow
      elif event.direction == "down":
        sense.show_letter("D") # Down arrow
      elif event.direction == "left":
        sense.show_letter("L") # Left arrow
      elif event.direction == "right":
        sense.show_letter("R") # Right arrow
      elif event.direction == "middle":
        sense.show_letter("M") # Enter key
    
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()