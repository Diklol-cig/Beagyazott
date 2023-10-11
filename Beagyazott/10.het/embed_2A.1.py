
import numpy as np
import cv2
import imutils
from imutils.video import VideoStream

prototxt_path = "./MobileNetSSD_prototxt.txt"
model_path = "./MobileNetSSD_deploy.caffemodel"

conf_limit = 0.25
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog",
           "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train",
           "tv/monitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Initialize the Pi Camera
vs = VideoStream(usePiCamera=True).start()

while True:
    frame = vs.read()

    if frame is None:  # Check if frame is None
        break

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    print("Sending frame through the network...")
    net.setInput(blob)
    detections = net.forward()

    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > conf_limit:
            idx = int(detections[0, 0, i, 1])
            # Rest of your object detection and annotation code here...

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vs.stop()
cv2.destroyAllWindows()
