import cv2 
import numpy

def preprocessing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    invert = cv2.bitwise_not(thresh)
    kernel = numpy.ones((1, 1), numpy.uint8)
    dilated = cv2.dilate(invert, kernel, iterations=2)

    return dilated