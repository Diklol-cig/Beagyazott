# Import necessary modules
from sense_hat import SenseHat
from time import sleep
import math

# Create an object from the SenseHat class
sense = SenseHat()

# Constants for altitude and Zambretti's algorithm
a = 0.0065
h = 125

# Initialize P0 variable
P0 = 0

# Acquire temperature, humidity, and pressure values in an infinite loop
while True:
    # Read temperature, pressure, and humidity values from the sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    P0 = (p * math.pow(1 - (0.0065 * h) / (t + (0.0065 * h) + 273.15),-5.257 ))

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # Calculate Zambretti's forecast number Z based on pressure tendency
    if p < P0 - 1.6:
        Z = 127 - (0.12 * P0)
    elif p > P0 + 1.6:
        Z = 185 - (0.16 * P0)
    else:
        Z = 144 - (0.13 * P0)

    # Determine the forecast based on Z value
    forecast = ""
    if 985 <= P0 <= 1050:
        if Z < 27:
            forecast = "Settled Fine"
        elif Z < 42:
            forecast = "Fine Weather"
        elif Z < 58:
            forecast = "Fine, Becoming Less Settled"
        elif Z < 73:
            forecast = "Fairly Fine, Showery Later"
        elif Z < 100:
            forecast = "Showery, Becoming More Unsettled"
        elif Z < 127:
            forecast = "Unsettled, Rain Later"
        elif Z < 144:
            forecast = "Rain at Times, Worse Later"
        elif Z < 175:
            forecast = "Rain at Times, Becoming Very Unsettled"
        else:
            forecast = "Very Unsettled, Rain"
    elif 960 <= P0 <= 1033:
        if Z < 29:
            forecast = "Settled Fine"
        elif Z < 44:
            forecast = "Fine Weather"
        elif Z < 60:
            forecast = "Fine, Possibly Showers"
        elif Z < 75:
            forecast = "Fairly Fine, Showers Likely"
        elif Z < 101:
            forecast = "Showery, Bright Intervals"
        elif Z < 127:
            forecast = "Changeable, Some Rain"
        elif Z < 144:
            forecast = "Unsettled, Rain at Times"
        elif Z < 175:
            forecast = "Rain at Frequent Intervals"
        else:
            forecast = "Very Unsettled, Rain"
    elif 947 <= P0 <= 1030:
        if Z < 31:
            forecast = "Settled Fine"
        elif Z < 46:
            forecast = "Fine Weather"
        elif Z < 62:
            forecast = "Becoming Fine"
        elif Z < 77:
            forecast = "Fairly Fine, Improving"
        elif Z < 103:
            forecast = "Fairly Fine, Possibly Showers Early"
        elif Z < 129:
            forecast = "Showery Early, Improving"
        elif Z < 144:
            forecast = "Changeable, Mending"
        elif Z < 175:
            forecast = "Rather Unsettled, Clearing Later"
        elif Z < 200:
            forecast = "Unsettled, Probably Improving"
        elif Z < 224:
            forecast = "Unsettled, Short Fine Intervals"
        elif Z < 250:
            forecast = "Very Unsettled, Finer at Times"
        else:
            forecast = "Stormy, Possibly Improving"
    elif P0 > 1030:
        forecast = "Stormy, Much Rain"
    else:
        forecast = "Unknown"

    # Create a message with the sensor values and weather forecast
    message = (
        "Temperature: " + str(t) + "C" + " Pressure: " + str(p) + "hPa" +
        " Humidity: " + str(h) + "%" + " Forecast: " + forecast +"P0: " + str(P0)
    )

    # Print the message
    print(message)

    # Sleep for one second before the next reading
    sleep(1)
