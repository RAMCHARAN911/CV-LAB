import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to binary image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Create structuring element (kernel)
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Binary Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Dilated Image", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 500, 350)
    cv2.resizeWindow("Binary Image", 500, 350)
    cv2.resizeWindow("Dilated Image", 500, 350)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Dilated Image", dilated)

    cv2.moveWindow("Original Image", 50, 100)
    cv2.moveWindow("Binary Image", 600, 100)
    cv2.moveWindow("Dilated Image", 1150, 100)

    # Save result
    cv2.imwrite("dilated_result.jpg", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
