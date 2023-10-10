from sense_hat import SenseHat
import time
import random

sense = SenseHat()

# Define colors
n = (0, 0, 0)
blue = (0, 0, 255)

# Initialize the LED matrix
matrix = [[n] * 8 for _ in range(8)]

def update_matrix():
    # Generate a random column index for the blue LED
    col = random.randint(0, 7)
    
    # Shift the first row down by one
    for row in range(7, 0, -1):
       matrix[row] = [pixel for pixel in matrix[row - 1]]
    
    # Turn on the LED in the first column of the first row with blue color
    matrix[0][col] = blue
    
def clear(): 
    # Clear the bottom row
    matrix[0] = [n] * 8

def main():
    while True:
        update_matrix()
        sense.set_pixels([pixel for row in matrix for pixel in row])
        time.sleep(0.5)
        clear()

if __name__ == "__main__":
    main()
