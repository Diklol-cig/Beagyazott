from pyzbar import pyzbar
import cv2

image_path = "./src.png"
image = cv2.imread(image_path)
barcodes = pyzbar.decode(image)
cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

for barcode in barcodes:
    # draw bounding box around the detected object
    (x, y, w, h) = barcode.rect
    #cv2.rectangle(image,(1,1),(1+w,1+h),(255,255,255),2)
    cv2.rectangle(image, (x, y), (x + w,y + h), (0, 0, 255), 2)
    # the barcode data is a bytes object so if we want to draw it on
    # our output image we need to convert it to a string first
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    print(barcode.rect)
    # draw the barcode description and type on the image
    text = "{} ({})".format(barcodeData, barcodeType)
    print(text)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imwrite("barcode.png", image)
