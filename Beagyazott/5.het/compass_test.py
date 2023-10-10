from matplotlib import pyplot as plt
from sense_hat import SenseHat
from time import sleep
import math

sense = SenseHat()

calibration = True

def stop():
    global calibration
    calibration = False

def plot(filename):
    # define two lists
    x_list = []
    y_list = []
    try:
        # open the file for read
        file = open(filename, 'r')
        # break file content into lines
        lines = file.readlines()

        # go through all lines
        for line in lines:
            values = line.split(',')
            x_list.append(float(values[0]))
            y_list.append(float(values[1]))
    finally:
        file.close()
    # max-min values
    xmax = max(x_list)
    xmin = min(x_list)
    ymax = max(y_list)
    ymin = min(y_list)
    print('Max x: ', xmax, 'Min x: ', xmin)
    print('Max y: ', ymax, 'Min y: ', ymin)

    line1, = plt.plot(range(1, len(x_list) + 1), x_list, 'r-', label='x')
    line2, = plt.plot(range(1, len(y_list) + 1), y_list, 'b--', label='y')
    plt.xlabel('Measurements')
    plt.ylabel('Value')
    plt.legend(handles=[line1, line2])
    plt.show()
    return xmax, xmin, ymax, ymin

def get_direction(deg):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    index = round(deg / 45)
    return directions[index % 8]

def main():
    filename = 'compass.txt'
    # open file for write (rewrite its content)
    file = open(filename, 'w')
    sense.stick.direction_middle = stop
    print('Start data acquisition...')
    # calibration process
    while calibration:
        magnet = sense.get_compass_raw()
        x = magnet['x']
        y = magnet['y']
        file.write(str(x) + ',' + str(y) + '\n')
    file.close()
    xmax, xmin, ymax, ymin = plot(filename)

    while True:
        magnet = sense.get_compass_raw()
        x = magnet['x']
        y = magnet['y']
        # range transform
        xz = -1 + ((1 - (-1)) / (xmax - xmin)) * (x - xmin)
        yz = -1 + ((1 - (-1)) / (ymax - ymin)) * (y - ymin)
        # degree (a) calculation

        if xz == 0 and yz < 0:
            deg = 90
        elif xz == 0 and yz > 0:
            deg = 270
        else:
            deg = math.degrees(math.atan2(yz, xz))
            if deg < 0:
                deg += 360

        # Get the direction
        direction = get_direction(deg)
        sense.show_message(direction, text_colour=[255, 255, 255])
        sleep(0.2)
        sense.clear()

if __name__ == "__main__":
    main()
