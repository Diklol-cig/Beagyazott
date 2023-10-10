from sense_hat import SenseHat
import time

sense = SenseHat()

p = [2,3]
light_len = 3
space_size = 8
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

def shift_right():
    # Iterate through the matrix rows
    for row in range(len(space)):
        # Iterate through the matrix columns
        for col in range(len(space[row])):
            if col < len(space[row]) - 1:
                # Shift 'r' values to the left by one column
                if space[row][col] == r and space[row][col + 1] == n:
                    space[row][col-1] = n
                    space[row][col + 1] = r
    sense.set_pixels(space)

def shift_left():
    # Iterate through the matrix rows
    for row in range(len(space)):
        # Iterate through the matrix columns
        for col in range(len(space[row])):
            if col < len(space[row]) - 1:
                # Shift 'r' values to the left by one column
                if space[row][col] == r and space[row][col + 1] == n:
                    space[row][col-1] = n
                    space[row][col + 1] = r
    sense.set_pixels(space)
def main():
    global p
    while True:
        while True:
            shift_right()
            time.sleep(speed)
            if p[0] == space_size-1: break
        while True:
            shift_left()
            time.sleep(speed)
            if p[0] == light_len-1: break
