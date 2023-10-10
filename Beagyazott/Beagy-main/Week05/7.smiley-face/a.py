from sense_hat import SenseHat
sense = SenseHat()

w = (255, 255, 255) # white
b = (0, 0, 255) # blue
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

