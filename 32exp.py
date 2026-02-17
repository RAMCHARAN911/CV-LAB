import cv2
import numpy as np

def colored_boxes(size):
    img = np.ones((size, size, 3), dtype=np.uint8) * 255
    box = size // 10

    img[0:box, 0:box] = [0,0,0]         # Black
    img[0:box, -box:] = [255,0,0]       # Blue
    img[-box:, 0:box] = [0,255,0]       # Green
    img[-box:, -box:] = [0,0,255]       # Red

    cv2.imshow("Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

colored_boxes(500)
