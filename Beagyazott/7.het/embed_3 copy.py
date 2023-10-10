from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.4
basket = [7, 4]
up_down = 1

w = (0, 0, 0)
r = (255, 0, 0)
b = (0, 0, 255)
game_space = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, b, b, w, w, w
]

def update_space(x, y, colour):
    # Index element from coordinate
    p = 8 * x + y
    game_space[p] = colour
    sense.set_pixels(game_space)

def left(event):
    if event.action == 'pressed':
        # The basket reached the left side
        if basket[1] - 1 == 0:
            pass
        # Move basket one position left
        else:
            update_space(basket[0], basket[1], w)
            basket[1] -= 1
            update_space(basket[0], basket[1] - 1, b)

def right(event):
    if event.action == 'pressed':
        # The basket reached the right side
        if basket[1] + 1 == 8:
            pass
        # Move basket one position left
        else:
            update_space(basket[0], basket[1] - 1, w)
            basket[1] += 1
            update_space(basket[0], basket[1], b)

sense.stick.direction_left = left
sense.stick.direction_right = right

sense.clear()
sense.set_pixels(game_space)
game_alive = True
score = 0
x = 0
while game_alive:

    # Initialize position and direction of the ball
    # (x,y) – ball coordinate, d - direction
    y = random.randint(0, 7)
    # random.choice() – randomly selects a value from a list
    d = random.choice([up_down, up_down])
    # put the ball into the game space
    update_space(x, y, r)
    # while the ball is in the game space
    while True:
        sleep(speed)
        update_space(x, y, w)
        # ball is on the edge of x dimension
        if x == 7:
            if y == basket[1] - 1 or y == basket[1]:
                # ball is in the basket
                update_space(x, y, b)
                score += 1
                up_down*=-1
                break
            else:
                # ball is out of the space
                game_alive = False
                break
        # ball reached the top or bottom of the space
        if y == 0 and up_down == -1:
            up_down = 1
        elif y == 7 and up_down == 1:
            up_down = -1
        y += up_down
        x += 1
        update_space(x, y, r)

sense.clear()
sense.show_message('Game over!', scroll_speed=0.05, back_colour=w)
sense.show_message('Score: ' + str(score), scroll_speed=0.05,back_colour=w)
