from sense_hat import SenseHat
import time

sense = SenseHat()

state = 0

w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
y = (255, 255, 0)
n = (0, 0, 0)

red = [
n, n, n, r, r, n, n, n,
n, n, n, r, r, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]
red_yellow = [
n, n, n, r, r, n, n, n,
n, n, n, r, r, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]
yellow = [
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, y, y, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]
green = [
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n,
n, n, n, g, g, n, n, n,
n, n, n, g, g, n, n, n
]

colors = [red, red_yellow, green, yellow]  # Define colors for states

def state_controller(duration):
    global state
    if state < len(colors):
        sense.set_pixels(colors[state])  # Set all LEDs to the current state color
        time.sleep(duration)
        state += 1
    else:
        state = 0
        sense.clear()

def sync_lights(event):
    global state
    if event.action == 'pressed':
        if state != 0:
            state = 0
        else:
            state = 3  # Start the synchronization

sense.stick.direction_middle = sync_lights

def main():
    global state
    while True:
        state_controller(1)  # Duration can be adjusted as needed

if __name__ == '__main__':
    main()
