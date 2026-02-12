import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((3, 3), np.uint8)

    # Apply dilation
    dilated_image = cv2.dilate(gray, kernel, iterations=1)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Dilated Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Dilated Image", 600, 400)

    # Show correct images
    cv2.imshow("Original Image", image)        # Real original
    cv2.imshow("Dilated Image", dilated_image)

    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Dilated Image", 750, 100)

    # Save result
    cv2.imwrite("dilated_image.jpg", dilated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
