import cv2
import numpy as np

def subtract_background(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0,0,0])
    upper = np.array([180,255,200])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Background Removed", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

subtract_background("image.jpg")
