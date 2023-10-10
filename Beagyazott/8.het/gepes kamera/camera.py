# Import opencv for computer vision stuff
import cv2
# Import matplotlib so we can visualize an image
from matplotlib import pyplot as plt
# Connect to capture device
cap = cv2.VideoCapture(3)
# Get a frame from the capture device
ret, frame = cap.read()
print(ret)

print(frame)
plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
plt.show()
# Releases capture back into the wild 
cap.release()
def take_photo(): 
    cap = cv2.VideoCapture(3)
    ret, frame = cap.read()
    cv2.imwrite('webcamphoto.jpg', frame)
    cap.release()

take_photo()