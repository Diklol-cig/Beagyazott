from sense_hat import SenseHat
import time

sense = SenseHat()

p = [3,2]
light_len = 3
space_size = 7
speed = 1/7

r = (255,0,0)
n = (0,0,0)
space = [
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
r, r, r, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]

def update_space(x, y, colour):
  #index element from coordinate
  l = 8 * x + y
  space[l] = colour
  sense.set_pixels(space)
  
def shift_right():
  update_space(p[0], p[1] - 2, n)
  update_space(p[0], p[1] - 1, n)

  p[1] += 1
  update_space(p[0], p[1], r)
  update_space(p[0], p[1]+1, r)

  print(p)

def shift_left():
  update_space(p[0],p[1],n)
  update_space(p[0],p[1]+1,n)

  p[1] -= 1
  update_space(p[0],p[1]-1,r)
  update_space(p[0],p[1]-2,r)

  print(p)

def main():
    global p
    while True:
        while True:
            shift_right()
            time.sleep(speed)
            if p[1] == space_size-1: break
        while True:
            shift_left()
            time.sleep(speed)
            if p[1] == light_len-1: break

if __name__ == "__main__":
    main()