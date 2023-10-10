from sense_hat import SenseHat
from time import sleep
import math

sense = SenseHat()


w = (255, 255, 255) # white
b = (0, 0, 255) # blue
r = (255, 0, 0) # red
g = (0, 255, 0) # green


cat1 = [
    w,w,w,w,w,w,w,w,
    r,w,w,w,w,w,w,w,
    w,r,w,w,r,w,r,w,
    w,r,g,g,r,b,b,w,
    w,g,g,g,b,w,b,g,
    w,g,g,g,g,b,b,w,
    w,g,w,g,w,g,w,w,
    w,w,w,w,w,w,w,w,
]


cat2 = [
    w,w,w,w,w,w,w,w,
    r,w,w,w,w,w,w,w,
    w,r,w,w,r,w,r,w,
    w,r,g,g,r,b,b,w,
    w,g,g,g,b,w,b,g,
    w,g,g,g,g,b,b,w,
    w,w,g,w,g,w,w,w,
    w,w,w,w,w,w,w,w,
]

def walk():
  for i in range(10):
    sense.set_pixels(cat1)
    sleep(1)
    sense.set_pixels(cat2)
    sleep(1)
    
while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
    F=math.sqrt(x*x+y*y+z*z)
    print(F)
    
    if F > 1.0:
      walk()


