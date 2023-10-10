import math
import time

import matplotlib.pyplot as plt
from sense_hat import SenseHat

sense = SenseHat()
calibration = True


def stop(event):
    global calibration
    if event.action == 'pressed':
        calibration = False


def plot(filename):
    x_list = []
    y_list = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(',')
            x_list.append(float(values[0]))
            y_list.append(float(values[1]))

    xmax, xmin = max(x_list), min(x_list)
    ymax, ymin = max(y_list), min(y_list)
    print('Max x:', xmax, 'Min x:', xmin)
    print('Max y:', ymax, 'Min y:', ymin)

    plt.plot(range(1, len(x_list) + 1), x_list, 'r-', label='x')
    plt.plot(range(1, len(y_list) + 1), y_list, 'b--', label='y')
    plt.xlabel('Measurements')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

    return xmax, xmin, ymax, ymin


def main():
    global calibration
    filename = 'compass.txt'

    with open(filename, 'w') as file:
        sense.stick.direction_middle = stop
        print('Start data acquisition...')

        while calibration:
            magnet = sense.get_compass_raw()
            x = magnet['x']
            y = magnet['y']
            file.write(str(x) + ',' + str(y) + '\n')
            time.sleep(0.1)

    xmax, xmin, ymax, ymin = plot(filename)

    while True:
        magnet = sense.get_compass_raw()
        x = magnet['x']
        y = magnet['y']

        xz = -1 + ((1 - (-1)) / (xmax - xmin)) * (x - xmin)
        yz = -1 + ((1 - (-1)) / (ymax - ymin)) * (y - ymin)

        if xz == 0 and yz < 0:
            deg = 90
        elif xz == 0 and yz > 0:
            deg = 270
        elif yz < 0:
            deg = 360 + math.atan2(yz, xz) * (180 / math.pi)
        else:
            deg = math.atan2(yz, xz) * (180 / math.pi)

        if deg < 22.5 or deg > 337.5:
            sense.show_letter('N', text_colour=[255, 0, 0])
        elif deg < 67.5:
            sense.show_letter('NE', text_colour=[255, 165, 0])
        elif deg < 112.5:
            sense.show_letter('E', text_colour=[0, 255, 0])
        elif deg < 157.5:
            sense.show_letter('SE', text_colour=[0, 255, 255])
        elif deg < 202.5:
            sense.show_letter('S', text_colour=[0, 0, 255])
        elif deg < 247.5:
            sense.show_letter('SW', text_colour=[75, 0, 130])
        elif deg < 292.5:
            sense.show_letter('W', text_colour=[148, 0, 211])
        else:
            sense.show_letter('NW', text_colour=[255, 0, 255])

        time.sleep(0.2)
        sense.clear()


if __name__ == '__main__':
    main()
