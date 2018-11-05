import matplotlib
import cv2
import sys

# from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

while True:
    cv2.imshow("sup", thresh)

    key = cv2.waitKey(0)
    if key == 27: #esc key quits out
        cv2.destroyAllWindows()
        sys.exit()