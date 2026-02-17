import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create structuring element
    kernel = np.ones((15, 15), np.uint8)

    # Apply Top Hat (Original - Opening)
    top_hat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

    # Save result
    saved = cv2.imwrite("tophat_result.jpg", top_hat)
    print("Image Saved:", saved)

    # Create windows
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Top Hat Result", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 500, 350)
    cv2.resizeWindow("Top Hat Result", 500, 350)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Top Hat Result", top_hat)

    # Arrange windows
    cv2.moveWindow("Original Image", 100, 100)
    cv2.moveWindow("Top Hat Result", 700, 100)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
