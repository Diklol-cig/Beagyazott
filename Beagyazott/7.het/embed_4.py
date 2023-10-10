import random
import time
from sense_hat import SenseHat

sense = SenseHat()

# Constants
WIDTH = 8
HEIGHT = 8
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Initialize game state
snake = [(4, 4)]  # Initial snake position
food = None
direction = (1, 0)  # Initial movement direction (right)

# Helper functions
def draw_pixel(x, y, color):
    sense.set_pixel(x, y, color)

def generate_food():
    global food
    while True:
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        if food not in snake:
            break

def move_snake():
    global snake, direction
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)
    if new_head == food:
        generate_food()
    else:
        snake.pop()

def check_collision():
    head = snake[0]
    if (
        head[0] < 0
        or head[0] >= WIDTH
        or head[1] < 0
        or head[1] >= HEIGHT
        or head in snake[1:]
    ):
        return True
    return False

def display_game():
    sense.clear()
    for segment in snake:
        draw_pixel(segment[0], segment[1], SNAKE_COLOR)
    draw_pixel(food[0], food[1], FOOD_COLOR)

def on_up(event):
    global direction
    if direction != (0, 1):
        direction = (0, -1)

def on_down(event):
    global direction
    if direction != (0, -1):
        direction = (0, 1)

def on_left(event):
    global direction
    if direction != (1, 0):
        direction = (-1, 0)

def on_right(event):
    global direction
    if direction != (-1, 0):
        direction = (1, 0)

def main():
    global direction
    sense.stick.direction_up = on_up
    sense.stick.direction_down = on_down
    sense.stick.direction_left = on_left
    sense.stick.direction_right = on_right

    generate_food()

    while True:
        move_snake()
        if check_collision():
            sense.show_message("Game Over")
            break
        display_game()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
