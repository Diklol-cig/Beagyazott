from sense_hat import SenseHat
import time

sense = SenseHat()
while True:
  #go throw all joystick’s events
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      # Check which direction
      if event.direction == "up":
        sense.show_letter("^") # Up arrow
      elif event.direction == "down":
        sense.show_letter("V") # Down arrow
      elif event.direction == "left":
        sense.show_letter("<") # Left arrow
      elif event.direction == "right":
        sense.show_letter(">") # Right arrow
      elif event.direction == "middle":
        sense.show_letter("M") # Enter key
    # Wait a while and then clear the screen
    time.sleep(0.5)
  sense.clear()

left_arrow = [
    0, 0, 0, 0, 0, 1, 0, 0,
    0, 0, 0, 0, 1, 1, 0, 0,
    0, 0, 0, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 1, 0, 0
]

right_arrow = [
    0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0
]
