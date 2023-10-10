from pyzbar import pyzbar
import cv2

# Initialize the video capture from the default camera (0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Detect barcodes and QR codes in the frame
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        # Draw bounding box around the detected code
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Extract barcode data and type
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # Display the barcode data and type on the frame
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame with detected codes
    cv2.imshow("Barcode/QR Code Scanner", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
