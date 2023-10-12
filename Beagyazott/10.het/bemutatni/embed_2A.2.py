import numpy as np
import cv2
import picamera
import picamera.array

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

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)  # Adjust the resolution as needed
    with picamera.array.PiRGBArray(camera) as stream:
        for frame in camera.capture_continuous(stream, format="bgr", use_video_port=True):
            image = frame.array
            (h, w) = image.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
            print("Sending image through the network...")
            net.setInput(blob)
            detections = net.forward()
            for i in np.arange(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > conf_limit:
                    idx = int(detections[0, 0, i, 1])
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                    print("{}".format(label))
                    cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
            
            cv2.imshow("Object Detection", image)
            key = cv2.waitKey(1) & 0xFF
            stream.truncate(0)
            
            if key == ord("q"):
                break

cv2.destroyAllWindows()
