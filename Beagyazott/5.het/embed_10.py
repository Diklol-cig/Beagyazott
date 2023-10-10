from sense_hat import SenseHat

sense = SenseHat()

while True:
  o = sense.get_orientation()
  acceleration = sense.get_accelerometer_raw()
  
  pitch = o["pitch"]
  roll = o["roll"]
  yaw = o["yaw"]
  
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
  x=round(x, 0)
  y=round(y, 0)
  z=round(z, 0)
  
  print("pitch: ", pitch, " roll: ", roll, " yaw: ", yaw)
  print("x: ", x, " y: ", y, " z: ", z)