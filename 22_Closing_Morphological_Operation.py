import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to binary
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Create structuring element
    kernel = np.ones((5, 5), np.uint8)

    # Apply Closing (Dilation followed by Erosion)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Save result
    saved = cv2.imwrite("closing_result.jpg", closing)
    print("Image Saved:", saved)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Binary Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Closing Result", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 500, 350)
    cv2.resizeWindow("Binary Image", 500, 350)
    cv2.resizeWindow("Closing Result", 500, 350)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Closing Result", closing)

    # Arrange windows
    cv2.moveWindow("Original Image", 50, 100)
    cv2.moveWindow("Binary Image", 600, 100)
    cv2.moveWindow("Closing Result", 1150, 100)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
