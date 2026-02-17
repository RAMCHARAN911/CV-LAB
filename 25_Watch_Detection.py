import cv2
import numpy as np

# Read main image
image = cv2.imread("watch.jpg")

# Read template (small cropped watch image)
template = cv2.imread("watch_template.jpg")

if image is None or template is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Get template size
    w, h = gray_template.shape[::-1]

    # Apply template matching
    result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

    # Set threshold
    threshold = 0.6
    loc = np.where(result >= threshold)

    # Draw rectangle where match found
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

    # Show result
    cv2.namedWindow("Watch Detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Watch Detection", 700, 500)
    cv2.imshow("Watch Detection", image)

    cv2.imwrite("watch_detected.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
