import cv2
import numpy as np

def add_text(size, text):
    img = np.ones((size,size,3), dtype=np.uint8)*255
    cv2.putText(img, text, (50, size//2),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0,0,0), 2)

    cv2.imshow("Text", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

add_text(500, "Hello OpenCV")
