# Import necessary modules
from sense_hat import SenseHat
from time import sleep

# Create an object from the SenseHat class
sense = SenseHat()

# Acquire temperature, humidity, and pressure values in an infinite loop
while True:
    # Get temperature, pressure, and humidity values from the sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # Create a message with the sensor values
    message = "Temperature: " + str(t) + "C" + " Pressure: " + str(p) + "hPa" + " Humidity: " + str(h) + "%"

    # Print the message
    print(message)

    # Sleep for one second before the next reading
    sleep(1)
