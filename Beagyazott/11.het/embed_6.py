import pytesseract
import cv2

image = cv2.imread("./test.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

options = "outputbase digits"
options += "-c tessedit_char_whitelist={} ".format("#")
options += "-c tessedit_char_blacklist={}".format("*")

text = pytesseract.image_to_string(image, config=options)
print(text)


