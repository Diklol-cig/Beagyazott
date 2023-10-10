from sense_hat import SenseHat

sense = SenseHat()

# Define constants
sea_level_pressure = 1013.25  # Standard atmospheric pressure at sea level in hPa
pressure_change_per_meter = 0.012  # Pressure change per 100 meters in kPa
pressure_change_per_meter_hPa = pressure_change_per_meter * 10  # Convert to hPa

# Get the current atmospheric pressure (in hPa)
current_pressure = sense.get_pressure()

# Calculate altitude using the International Barometric Formula
altitude = 44331 * (1 - pow((current_pressure / sea_level_pressure), 1/5.2558))

# Print the predicted altitude
print(f"Predicted Altitude: {altitude:.2f} meters")
