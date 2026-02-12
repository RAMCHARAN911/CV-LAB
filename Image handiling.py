import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale (for erosion)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((3, 3), np.uint8)

    # Apply erosion
    eroded_image = cv2.erode(gray, kernel, iterations=1)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Eroded Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Eroded Image", 600, 400)

    # 🔥 IMPORTANT:
    cv2.imshow("Original Image", image)        # Show REAL color image
    cv2.imshow("Eroded Image", eroded_image)   # Show eroded result

    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Eroded Image", 750, 100)

    cv2.imwrite("eroded_image.jpg", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
