# Import necessary libraries
from sense_hat import SenseHat
import matplotlib.pyplot as plt
import time

# Define the data visualization function which reads data from a file
def plot(filename):
    # Define two lists to store temperature and humidity data
    temp_list = []
    humi_list = []
    
    try:
        # Open the file for reading
        file = open(filename, 'r')
        
        # Break file content into lines
        lines = file.readlines()
        
        # Go through all lines and split lines by ','
        for line in lines:
            values = line.split(',')
            temp_list.append(float(values[0]))
            humi_list.append(float(values[1]))
    finally:
        file.close()
    
    # Create a graph using the plot function from matplotlib
    plt.plot(range(1, len(temp_list) + 1), temp_list, 'r-', label='Temperature (C)')
    plt.plot(range(1, len(humi_list) + 1), humi_list, 'b--', label='Humidity (%)')
    plt.title('Weather Data')
    plt.xlabel('Measurements')
    plt.ylabel('Value')
    plt.legend()  # Show legend with labels
    plt.show()

# Data acquisition is in the main() function
def main():
    sense = SenseHat()
    
    # Get the current time
    start_time = time.time()
    stop_time = time.time()
    
    filename = 'weather.txt'
    
    # Open the file for append
    file = open(filename, 'a')
    
    print('Data acquisition is starting...')
    
    while stop_time - start_time < 5:
        file.write(str(sense.get_temperature()) + ',' + str(sense.get_humidity()) + '\n')
        time.sleep(0.5)  # Wait for 0.5 seconds
        stop_time = time.time()
    
    print('Stop data acquisition!')
    file.close()
    
    # Call the plot function to visualize the data
    plot(filename)

if __name__ == '__main__':
    main()
