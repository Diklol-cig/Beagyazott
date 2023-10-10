from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

w = (0, 0, 0) # white
r = (255,0,0)

while True:
  #go throw all joystick’s events
  for event in sense.stick.get_events():
  # Check if the joystick was pressed
    if event.action == "pressed":
      # Check which direction
      if event.direction == "up":
        # Set up how the image look like
        smiley_pixels = [
         w, w, w, r, w, w, w, w,
         w, w, r, r, r, w, w, w,
         w, r, w, r, w, r, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w]
         
        # change all 64 LEDs
        sense.set_pixels(smiley_pixels)
        
      elif event.direction == "down":
        smiley_pixels = [
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, w, w, r, w, w, w, w,
         w, r, w, r, w, r, w, w,
         w, w, r, r, r, w, w, w,
         w, w, w, r, w, w, w, w]
         
        # change all 64 LEDs
        sense.set_pixels(smiley_pixels)
      elif event.direction == "left":
        smiley_pixels = [
         w, w, w, w, w, w, w, w,
         w, w, w, w, w, w, w, w,
         w, w, r, w, w, w, w, w,
         w, r, w, w, w, w, w, w,
         r, r, r, r, r, r, r, r,
         w, r, w, w, w, w, w, w,
         w, w, r, w, w, w, w, w,
         w, w, w, w, w, w, w, w]
         
        # change all 64 LEDs
        sense.set_pixels(smiley_pixels)
      elif event.direction == "right":
        smiley_pixels = [
         w, w, w, w, w, w, w, w,
         w, w, w, w, w, w, w, w,
         w, w, w, w, w, r, w, w,
         w, w, w, w, w, w, r, w,
         r, r, r, r, r, r, r, r,
         w, w, w, w, w, w, r, w,
         w, w, w, w, w, r, w, w,
         w, w, w, w, w, w, w, w]
         
        # change all 64 LEDs
        sense.set_pixels(smiley_pixels)
    
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()