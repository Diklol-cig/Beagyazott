from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()

o = (0,0,0) #no color
b = (0,0,255)

one_img = [o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,b,b,o,o,o,
           o,o,o,b,b,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o]

two_img = [o,o,o,o,o,o,o,o,
           o,b,b,o,o,o,o,o,
           o,b,b,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,b,b,o,
           o,o,o,o,o,b,b,o,
           o,o,o,o,o,o,o,o]
           
three_img = [b,b,o,o,o,o,o,o,
             b,b,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,b,b,o,o,o,
             o,o,o,b,b,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,b,b,
             o,o,o,o,o,o,b,b]

four_img =  [b,b,o,o,o,o,b,b,
             b,b,o,o,o,o,b,b,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             b,b,o,o,o,o,b,b,
             b,b,o,o,o,o,b,b]
             
             

five_img =  [b,b,o,o,o,o,b,b,
             b,b,o,o,o,o,b,b,
             o,o,o,o,o,o,o,o,
             o,o,o,b,b,o,o,o,
             o,o,o,b,b,o,o,o,
             o,o,o,o,o,o,o,o,
             b,b,o,o,o,o,b,b,
             b,b,o,o,o,o,b,b]


six_img =   [b,b,o,b,b,o,b,b,
             b,b,o,b,b,o,b,b,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             b,b,o,b,b,o,b,b,
             b,b,o,b,b,o,b,b]
             
numbers = (one_img,two_img,three_img,four_img,five_img,six_img)       
             
def cycle():
    for i in range(3):
      val = random.randint(1,6)
      sense.set_pixels(numbers[val])
      sleep(0.1)


def number_gen(event):
    global numbers
    if event.action == "pressed":
      val = random.randint(1,6)
      print(val)
      sense.set_pixels(numbers[val])
    sleep(2)
    sense.clear()
    
    
while True:
  for event in sense.stick.get_events():
    number_gen(event)